   import requests
   from bs4 import BeautifulSoup

   def scrape_web(url):
       response = requests.get(url)
       soup = BeautifulSoup(response.text, 'html.parser')
       return soup.prettify()