import requests
from bs4 import BeautifulSoup

def scrape_web(url):
    """
    Scrape a web page and return its content in a structured format.

    Args:
        url (str): The URL of the web page to scrape.

    Returns:
        str: The structured content of the web page.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.prettify()