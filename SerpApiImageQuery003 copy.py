import requests
import os
import requests
import random
from bs4 import BeautifulSoup
import webbrowser

def search_and_open_image_urls(query):
    # Make a request to the webpage
    response = requests.get(query)
    soup = BeautifulSoup(response.text, "html.parser")
    # Find all the anchor tags in the webpage
    anchor_tags = soup.find_all("a")

    # Filter the anchor tags to get the ones containing "imgur" in the URL
    imgur_urls = [tag["href"] for tag in anchor_tags if "imgur" in tag["href"]]

    # Open each imgur URL in a web browser
    for imgur_url in imgur_urls:
        webbrowser.open(imgur_url)

# Call the function with the desired query
query = "https://www.plurk.com/s/u/hugerisme?offset=1649610040&last_offset=1680509436"
search_and_open_image_urls(query)

