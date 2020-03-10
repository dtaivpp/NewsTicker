
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

valid_descendants = {'p', 'li', 'td', 'a'}

def recusive_search(root_element):
    for descendent in root_element.descendants:
        if descendent.name in valid_descendants:
            # Need a better way to isolate releated elements? 
            # Possibly a specific scrape per site? 
            print(descendent.text)

def page_scrape(url, *article_identifier):
    # Pull out the content of the page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    root_article_element = soup.find(article_identifier)
    
    text = recusive_search(root_article_element)
        
    pass



if __name__=="__main__":
    page_scrape("https://www.bloomberg.com/news/articles/2020-03-09/stock-rout-to-continue-in-asia-after-u-s-plunge-markets-wrap?srnd=premium", "div", {"class": "body-copy-v2 fence-body"})
    page_scrape("https://finance.yahoo.com/news/why-cheering-the-crash-in-oil-prices-like-trump-just-did-is-oversimplifying-the-risks-203530179.html")