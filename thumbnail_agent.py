#ai agents creat thumbnails ;

from google import genai
import json 
from google.genai import types
client = genai.Client()
import requests
import base64
import os

while True:
    ask = input("enter the video title : ").strip()
    if ask == "":
        print("please enter a valid title :)")
    else:
        break

try:
 response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=f""" 
    Generate exactly 3 creative YouTube thumbnail concepts
    for this video title: {ask}

    Return valid JSON only, using this structure:
     {{
     "ideas": [
     {{
      "name": "Idea name",
      "visual_composition": "Describe the visual",
      "text_overlay": "Maximum 4 words",
      "colors": ["color1", "color2"],
      "why_click": "Why viewers might click"
     }}
     ]
      }}

     Include exactly 3 objects inside the ideas array.
     Do not use Markdown fences or explanations outside the JSON.
     Do not invent earnings or results.
    """
 )
 print(response.text)

except Exception as error:
    print("Gemini is temporarily unavailable.")
    print("Error:", error)
    exit()
try:
    data = json.loads(response.text)
    ideas = data["ideas"]

    if len(ideas) != 3:
        raise ValueError("Gemini did not return exactly 3 ideas.")

except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
    print("Could not read the ideas correctly.")
    print("Error:", error)
    print("Gemini response:", response.text)
    raise SystemExit

# Display the three ideas
for number, idea in enumerate(ideas, start=1):
    print(f"\n--- Idea {number}: {idea['name']} ---")
    print("Visual:", idea["visual_composition"])
    print("Thumbnail text:", idea["text_overlay"])
    print("Colors:", ", ".join(idea["colors"]))
    print("Why click:", idea["why_click"])

# Ask the user to choose
while True:
    choice = input("\nChoose an idea (1, 2, or 3): ").strip()

    if choice in ["1", "2", "3"]:
        break

    print("Invalid choice. Please enter 1, 2, or 3.")

# Retrieve the exact idea selected
selected_idea = ideas[int(choice) - 1]

print(f"\nYou selected: {selected_idea['name']}")

# Develop that exact idea
idea_name = selected_idea["name"]
visual = selected_idea["visual_composition"]
thumbnail_text = selected_idea["text_overlay"]
colors = ", ".join(selected_idea["colors"])

try:
    second_res = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f"""
        Create a detailed image-generation prompt.

        Video title: {ask}
        Concept name: {idea_name}
        Visual composition: {visual}
        Thumbnail text: {thumbnail_text}
        Main colors: {colors}

        Include:
        - Detailed composition and subject placement
        - Lighting and background
        - Facial expression if relevant
        - Professional design
        - 16:9 aspect ratio

        Preserve the selected concept.
        Do not invent earnings or results.
        """
    )

    print("\n--- Detailed Image Prompt ---")
    print(second_res.text)

except Exception as error:
    print("Something went wrong while generating the detailed prompt.")
    print("Error:", error)

while True:
    generate = input("Do you want to generate this thumbnail? (yes/no): ").strip().lower()
    if generate in ["yes", "no"]:
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

 #  send description to cloudflare api to generate the image and return the image in base64 format
def generate_image(prompt):

    account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID")
    api_token = os.getenv("CLOUDFLARE_API_TOKEN")
    print("Account ID exists:", bool(account_id))
    print("API Token exists:", bool(api_token))

    url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/black-forest-labs/flux-1-schnell"

    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    data = {
        "prompt": prompt
    }

    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    return response
#confirmation and call the function to generate the image and save it as thumbnail.png
if generate == "yes":
    print("Generating your thumbnail...")

    try:
        image_response = generate_image(second_res.text)

        if image_response.status_code == 200:
            result = image_response.json()

            image_bytes = base64.b64decode(result["result"]["image"])

            with open("Downloads/python/thumbnail.png", "wb") as file:
                file.write(image_bytes)

            print("Thumbnail saved successfully!")

        else:
            print("Image generation failed:")
            print(image_response.text)

    except Exception as error:
        print("Something went wrong:", error)

else:
    print("Thumbnail generation canceled.")
