from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import shutil
from test_image_detection import recognize_items, generate_zero_waste_recipe
from models import User, Food
from datetime import datetime, timedelta
import uuid 


# CRUD TO DB!!

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

# check what kind of food you have
@app.route("/detect-food", methods=["POST"])
def detect_food():
    if "file" not in request.files:
        return jsonify({"result": "No file uploaded"}), 400

    file = request.files["file"]
    os.makedirs("images", exist_ok=True)
    file_path = os.path.join("images", file.filename)
    file.save(file_path)

    items = recognize_items(file_path)
    if not items.items:
        return jsonify({"result": "Food could not be detected."})

    result_list = [
        {"name": f.name, "quantity": f.quantity, "expiration": str(f.expiration)}
        for f in items.items
    ]
    return jsonify({"result": result_list})


# create a (zero waste) recipe
@app.route("/zero-waste-recipe", methods=["POST"])
def zero_waste_recipe():
    if "file" not in request.files:
        return jsonify({"result": "No file uploaded"}), 400

    file = request.files["file"]
    os.makedirs("images", exist_ok=True)
    file_path = os.path.join("images", file.filename)
    file.save(file_path)

    result = generate_zero_waste_recipe(file_path)
    return jsonify({"result": result})


# adding a user
@app.route("/add-to-db", methods=['POST'])
def add_to_db():
    data = request.json

    username = data.get("username")
    name = data.get("name")
    password = data.get("password")

    if not username or not name or not password:
        return jsonify({"result": "username, name, and password are required"}), 400

    # check for duplicates
    if User.objects(username=username).first():
        return jsonify({"result": f"User {username} already exists"}), 400

    user = User(username=username, name=name, password=password)
    user.save()

    return jsonify({"result": f"User {username} added successfully", "id": str(user.id)})


@app.route("/add-food", methods=['POST'])
def add_food():
    data = request.json

    user_id = data.get("_id")  # UUID string from client
    name = data.get("name")
    quantity = data.get("quantity")
    shelf_life_days = data.get("shelf_life", 5)

    if not user_id or not name or not quantity:
        return jsonify({"result": "_id, name, and quantity are required"}), 400

    # Convert string to UUID object
    try:
        user_uuid = uuid.UUID(user_id)
    except ValueError as e:
        return jsonify({"result": f"Invalid _id format: {e}"}), 400

    # Find user by UUID
    user = User.objects(id=user_uuid).first()
    if not user:
        return jsonify({"result": f"User {user_id} not found"}), 404

    # Create food
    expiration_date = datetime.now() + timedelta(days=shelf_life_days)
    food = Food(
        user=user,
        name=name,
        quantity=quantity,
        expiration_date=expiration_date
    )
    food.save()

    return jsonify({
        "result": f"Food {name} added for user {user.username}",
        "food_id": str(food.id),
        "expiration_date": expiration_date.strftime("%Y-%m-%d")
    })

if __name__ == "__main__":
    app.run(debug=True, port=8000)
