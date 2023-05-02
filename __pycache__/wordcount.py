from collections import Counter
import requests
from bs4 import BeautifulSoup
import json

def word_frequency(url):
    # Send GET request to the URL
    page = requests.get(url)

    # Use BeautifulSoup to parse the HTML content of the page
    soup = BeautifulSoup(page.content, 'html.parser')

    # Extract the text content from the page
    text = soup.get_text()

    # Split the text into words
    words = text.split()

    # Count the frequency of each word using Counter
    word_count = Counter(words)

    # Convert the Counter object to a dictionary
    word_dict = dict(word_count)

    # Encode the dictionary as JSON
    word_json = json.dumps(word_dict, sort_keys=True, indent=4)

    # Return the JSON string
    return word_json
