import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('SPOONACULAR_API_KEY')

def get_live_recipe(food_item):
    url = f"https://api.spoonacular.com/recipes/complexSearch?query={food_item}&number=1&apiKey={API_KEY}"
    try:
        response = requests.get(url)
        # Check if the API key actually worked (Status 200 is success)
        if response.status_code == 200:
            data = response.json()
            if data.get("results"):
                return data["results"][0]["title"]
        return None
    except:
        return "error"

def smart_chef_app():
    print("--- 👨‍🍳 Welcome to the LIVE Smart Chef! 👩‍🍳 ---")
    
    # Simple list of 'filler' words to ignore
    conversational_words = ["yes", "no", "maybe", "sure", "ok", "cool", "thanks", "thank you"]

    while True:
        print("\n" + "-"*30)
        user_input = input("Chef: What's on your mind? ").lower().strip()

        if user_input == 'quit':
            print("Chef: Goodbye! Come back when you're hungry!")
            break

        # 1. Handle Greetings & Small Talk
        if any(word in user_input for word in ["hi", "hello", "hey", "yo"]):
            print("Chef: Hello! I'm ready. What ingredients do we have today?")
            continue
        
        # 2. Handle "Filler" words (Fixing your 'Yes' bug)
        if user_input in conversational_words:
            print("Chef: Great! Tell me a specific food or ingredient you're thinking of.")
            continue

        # 3. Handle specific non-food questions
        if "who are you" in user_input:
            print("Chef: I'm your digital sous-chef! I search the web to find you meals.")
            continue
        if "surprise" in user_input:
            print("Chef: Ooh, a risk-taker! Let me find something random...")
            continue         

        # 4. If it's none of the above, try searching the API
        print(f"Chef: Let me check my cookbook for '{user_input}'...")
        recipe_title = get_live_recipe(user_input)

        if recipe_title == "error":
            print("Chef: Oops! I lost my connection to the kitchen. Check your internet/API key.")
        elif recipe_title:
            print(f"\n[FOUND] I found a recipe for: {recipe_title}!")
            print("Chef: Does that sound good, or do you want to try another ingredient?")
        else:
            print(f"\nChef: I couldn't find a recipe for '{user_input}'. Is it a typo, or something rare?")

        time.sleep(0.5) # This will work now because we imported time!

if __name__ == "__main__":
    smart_chef_app()