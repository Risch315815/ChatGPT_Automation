import os
import requests
import os
import requests
import random

def search_and_download_image(query, directory):
    # Make a request to SerpApi to search for images
    api_key = "c3fa39df7a1e9fa6eb9744a711c7333ebe7ceece4465f6034bbfb6f73feb7af0"
    search_url = f"https://serpapi.com/search.json?q={query}&tbm=isch&api_key={api_key}"
    response = requests.get(search_url)
    data = response.json()
    K = 0

    # Check if the response contains any images
    if "images_results" in data:
        # Get the URLs of all the images
        image_urls = [result["original"] for result in data["images_results"]]

        # Download each image
        for image_url in image_urls:
            image_data = requests.get(image_url).content

            #edit query name as a part of path name
            Q_name = directory+"/"+locals()["query"][:5]

            # Create the directory if it doesn't exist
            os.makedirs(Q_name, exist_ok=True)

            # Save the image to the specified directory
            image_path = os.path.join(f"{Q_name}/{query[-4:]}_{K}.jpg")
            print(image_path)

            with open(image_path, "wb") as file:
                file.write(image_data)
            K += 1
            print(f"Image downloaded successfully for {query}")

        print(f"Image downloaded successfully to {image_path}")
    else:
        print("No images found for the given query")

# Example usage
#search_and_download_image("cat", "D:/Coding/SystemPromptChatGPT/AnimalImg")

def search_and_download_images(query_list, directory):
    # Make a request to SerpApi for each query in the list
    api_key = "c3fa39df7a1e9fa6eb9744a711c7333ebe7ceece4465f6034bbfb6f73feb7af0"
    for query in query_list:
        search_url = f"https://serpapi.com/search.json?q={query}&tbm=isch&api_key={api_key}"
        response = requests.get(search_url)
        data = response.json()

        # Check if the response contains any images
        if "images_results" in data:
            # Get the URL of the first image
            image_url = data["images_results"][0]["original"]

            # Download the image
            image_data = requests.get(image_url).content

            # Create the directory if it doesn't exist
            os.makedirs(directory, exist_ok=True)

            # Save the image to the specified directory
            image_path = os.path.join(directory, f"{query}.jpg")
            with open(image_path, "wb") as file:
                file.write(image_data)

            print(f"Image downloaded successfully for {query}")
        else:
            print(f"No images found for {query}")

# Example usage
query_list = ["cat", "dog", "bird"]
#search_and_download_images(query_list, "D:/Coding/SystemPromptChatGPT/AnimalImg")

Hugger = [["Huger_Smot", "twitter"], ["huger_smot", "e621"], ["hugerisme", "plurk"]]

for i in Hugger:
    Query00 = f"{i[0]}, inurl:{i[1]}"
    search_and_download_image(Query00, "D:/Coding/SystemPromptChatGPT/AnimalImg")

