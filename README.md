# technica-2025
Devpost: https://devpost.com/software/food-scanner-d5j9f0

## 🌟 Inspiration
We all buy a bunch of groceries … and then forget what’s in the fridge after a few days. In fact, the average U.S. household wastes about **30%** of the food they buy. On top of that, Americans toss about **103** pounds of spoiled food from their refrigerator every year, equivalent to roughly four items per week and **77%** of people say it's because they simply forgot what was in there. That’s a lot of edible food going to waste. We wanted to create a solution that gives you full control and insight into your fridge: What did you put in? When does it expire? How can you use items before they go bad? **Enter freshly yours: an app that helps you manage your fridge, stay healthy, and reduce food waste by suggesting recipes using your soon-to-expire ingredients. Zero waste has never been easier or tastier. It's all fresh, and all yours! ♡**

## 🛠️ What it does
Our application, freshly yours, is designed to help users track and manage their food purchases effortlessly. Users can add items in multiple ways:
1. Upload a photo. OpenAI identifies the food items and their quantities.
2. Voice input. Powered by ElevenLabs, users can say something like “I bought 10 apples today,” and the app automatically logs the items. This also serves as an accessibility feature for users who prefer or rely on voice interaction.
3. Scan grocery receipts. Text is extracted and cross-checked with the USDA Food Data API to ensure only valid food items are logged.
4. Manual entry. Users can log foods they buy by filling out a form.

Once an item is identified, the app calculates its approximate expiration date by combining the purchase date with the item’s recommended fridge shelf life. If a food item is approaching expiration (within 1–2 days), the app sends a notification and suggests zero-waste recipes using the Spoonacular API, helping users reduce food waste efficiently.

## 🧱 How we built it
- Frontend: Built with React and Vite.
- Backend: A Python Flask server ties backend logic with our MongoDB database.
- AI: We integrated OpenAI to help detect the correct foods within images and suggest zero food waste recipes. We also used ElevenLabs speech recognition for hands-free voice logging of grocery items.
- APIs: We integrated Spoonacular and Open AI APIs to get recipe suggestions and detect food names, and we used ElevenLabs + Gemini AI to record user speech and update food data.
- Data Sources: We incorporated the USDA FSIS FoodKeeper JSON dataset, parsing it to retrieve accurate shelf-life recommendations for each food item in your fridge.

## ⚔️ Challenges we ran into
We encountered several significant challenges during development. Integrating the frontend with the backend proved tricky, particularly due to CORS issues when attempting to reach our endpoints. Additionally, we faced incompatibilities with Next.js components, which ultimately led us to switch to Vite for smoother integration. Handling components that required complex input—such as camera captures and receipt scanning—was also challenging. Determining which items were actually food was difficult without leveraging an API to parse and verify the data, adding an extra layer of complexity to ensuring accuracy and usability.

## 🎖️Our Accomplishments
- **Automated, accessible data entry**: users can upload data via photos of their food or receipts, purely by voice input (no hands needed!); there is also a manual input option as a fallback
- **Connected to database**: website shows uploaded data in real time, including summary statistics and the full list
- **Visualize food expiration**: see calculated expiry dates and days left for all of your food
- **Branded, stylized and functional UI**: to emphasize ease of use, designed to work for mobile (primary) and desktop (secondary) screens 
- **Displaying zero-waste recipes**: for utilizing your fridge
- **Efficient development**: Git pull requests and collaboration, and Gen AI for code planning + implementation

## What we learned
- new food APIs/datasets: Spoonacular and USDA FoodKeeper
- new tool for incorporating function to speech: ElevenLabs
- new knowledge about the food space and zero waste eating!
- using Figma Make for UI design

## What's next for freshly yours
- Adding recipe recommendations based on allergens, cuisine preferences, etc
- More visualizations of your food data: by food group, expiration dates, etc
- Notifications for when your food is expiring soon
- Building out an integrated shopping cart helper
