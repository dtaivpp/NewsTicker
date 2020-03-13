from bs4 import BeautifulSoup
import lxml
import os
import json
from util.domain_tools import extract_domain

valid_descendants = {'p', 'li', 'td', 'a'}

def recusive_search(root_element):
    '''Find the text values of all article elements'''
    for descendent in root_element.descendants:
        if descendent.name in valid_descendants:
            # Need a better way to isolate releated elements? 
            # Possibly a specific scrape per site? 
            print(descendent.text)



def element_to_target(url):
    '''Returns an object with parameters used to extract the article text'''
    config_data = {}

    configpath = os.path.join(os.curdir,'src','config', 'scrape.config')
    with open(configpath, 'r') as config_handle:
        config_data = json.load(config_handle)

    domain_name = extract_domain(url)

    if domain_name in config_data:
        return config_data[domain_name]

    return None



def page_processer(request):
    '''Returns Article Text'''
    # Pull out the content of the page
    article_identifier = element_to_target(request.url)

    soup = BeautifulSoup(request.text, 'lxml')
    
    # Query config file for type of identifier needed
    root_article_element = soup.find(article_identifier)

    text = recusive_search(root_article_element)
        
    return text


if __name__=="__main__":
    # Load up test pages
    from util.load_test_page import get_test_requests
    
    request_list = get_test_requests()

    for page in request_list:
        page_processer(page)