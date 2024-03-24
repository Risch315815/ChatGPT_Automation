from openai import OpenAI
import shutil

API_KEY = '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'
client = OpenAI(api_key = API_KEY)

def sendMessages(Prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=Prompt,
        temperature=0
    )
    response_message = response.choices[0].message.content
    return response_message

def Messages(Premise, Order):
    messages = [
    {"role": "system", "content": Premise},
    {"role": "user", "content": "hey"},
    {"role": "assistant", "content": "hey, nice to meet you. What can I do for you today?"},
    {"role": "user", "content": Order},
    ]
    return messages

#-------------------------------------------------------
premise00 = "You are a professional zoologist. You job is to answer all of the questions regarding names of species using 'Binomial nomenclature' and nothing else."
order00 = "Please list 5 random animals in the form of [a, b, c, d, e]. Please just list the names of the animals, and nothing else. Do not use bullet or numeric or alphabetics, and do not include introduction. "
order01 = "Please make a list of 5 animals most closely related to each of the animals in the list in the form of [a, b, c, d, e, ....]. Please just append the names of the animals behind the names of the animals in the original list, and nothing else. Do not use bullet or numeric or alphabetics, and do not include introduction."
ans1 = sendMessages(Messages(premise00, order00))
sequ = [0]
sequ[0] = ans1
print(ans1)
for i in (0, 1, 2, 3):
    ansx = sendMessages(Messages(sequ[i], order01))
    sequ.append(ansx)
print(sequ[3])

#-------------------------------------------------------
fileA = 'D:/Coding/SystemPromptChatGPT/AnimalNameOri.txt'
fileB = 'D:/Coding/SystemPromptChatGPT/AnimalName.txt'
fileC = 'D:/Coding/SystemPromptChatGPT/AnimalNameTrim.txt'

with open(fileA, 'w') as file001:
    file001.write(sequ[3])
    file001.close()

with open(fileB, 'r') as file001:
    content = file001.read()
    trimmed_content = content.replace(':', ', ')
    unique_items = set(trimmed_content.split(', '))
    trimmed_content = ', '.join(unique_items)

with open(fileB, 'w') as file002:
    file002.write(trimmed_content)
    file002.close()

#-------------------------------------------------------

import requests
import os
from bs4 import BeautifulSoup
website = ""

import serpapi
from serpapi import GoogleSearch
API_KEY = "c3fa39df7a1e9fa6eb9744a711c7333ebe7ceece4465f6034bbfb6f73feb7af0"
params = {
    "engine": "google",
    "q": "ice cream",
    "api_key": API_KEY}

# Read the animal names from the file
animal_file = 'D:/Coding/SystemPromptChatGPT/AnimalNameTrim.txt'
with open(animal_file, 'r') as file:
    animal_names = file.read().split(', ')

# Create a directory to save the images
image_dir = 'D:/Coding/SystemPromptChatGPT/AnimalImg'
os.makedirs(image_dir, exist_ok=True)

# Search and save images for each animal
for animal_name in animal_names:
    search_query = f"{animal_name} image"
    search_params = {
        "engine": "google",
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
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(image_path, 'wb') as file:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, file)
            print(f"Image saved for {animal_name}")
        else:
            print(f"Failed to download image for {animal_name}")
    else:
        print(f"No image found for {animal_name}")