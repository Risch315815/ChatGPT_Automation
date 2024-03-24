import requests
import os
from serpapi import GoogleSearch
import shutil

website = ""

API_KEY = "c3fa39df7a1e9fa6eb9744a711c7333ebe7ceece4465f6034bbfb6f73feb7af0"
params = {
    "engine": "google",
    "q": "ice cream",
    "api_key": API_KEY}

animal_names = ['Stegodon trigonocephalus','Neofelis nebulosa', 'Loxodonta cyclotis', 'Ursus thibetanus']

# Create a directory to save the images
image_dir = 'D:/Coding/SystemPromptChatGPT/AnimalImg'

# Search and save images for each animal
for animal_name in animal_names:
    search_query = f"{animal_name} image"
    search_params = {
        "engine": "google_image",
        "q": search_query,
        "api_key": API_KEY
    }
    search = GoogleSearch(search_params)
    results = search.get_dict().get('images_results', [])

    if results:
        image_url = results[0].get('original')
        image_name = f"{animal_name}.jpg"
        image_path = os.path.join(image_dir, image_name)

        # Download and save the image
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(image_url, headers=headers, stream=True)
        if response.status_code == 200:
            with open(image_path, 'wb') as file:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, file)
            print(f"Image saved for {animal_name}")
        else:
            print(f"Failed to download image for {animal_name}")
    else:
        print(f"No image found for {animal_name}")
