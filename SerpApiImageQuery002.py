import requests
import os
import requests
import random
from bs4 import BeautifulSoup

def search_and_download_image(query, directory):
    # Make a request to the webpage
    response = requests.get(query)
    soup = BeautifulSoup(response.text, "html.parser")
    # Find all the anchor tags in the webpage
    anchor_tags = soup.find_all("a")

    # Filter the anchor tags to get the ones containing "imgur" in the URL
    imgur_urls = [tag["href"] for tag in anchor_tags if "imgur" in tag["href"]]

    # Download each image from the imgur URLs
    for i, imgur_url in enumerate(imgur_urls):
        # Make a request to the imgur URL
        imgur_response = requests.get(imgur_url)
        imgur_data = imgur_response.content

        # Create the directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)
        Q_name = directory+"/"+imgur_urls[i][-8:]
        print(imgur_urls[i])
        print(Q_name)

        # Save the image to the specified directory
        image_path = os.path.join(Q_name)
        with open(image_path, "wb") as file:
            file.write(imgur_data)

        print(f"Image downloaded successfully: {imgur_url}")
    print(f"All images downloaded successfully to {directory}")

# Call the function with the desired query and directory
query = "https://www.plurk.com/s/u/hugerisme?offset=1649610040&last_offset=1680509436"
directory = "D:/Coding/SystemPromptChatGPT/AnimalImg"
search_and_download_image(query, directory)
        
# Query00 = "https, inurl:https://www.plurk.com/s/u/hugerisme"
# search_and_download_image(Query00, "D:/Coding/SystemPromptChatGPT/AnimalImg")

