from bs4 import BeautifulSoup
import lxml
import os
import pickle

valid_descendants = {'p', 'li', 'td', 'a'}

def recusive_search(root_element):
    for descendent in root_element.descendants:
        if descendent.name in valid_descendants:
            # Need a better way to isolate releated elements? 
            # Possibly a specific scrape per site? 
            print(descendent.text)


def page_processer(request):
    # Pull out the content of the page

    soup = BeautifulSoup(request.text, 'lxml')
    
    # Query config file for type of identifier needed
    root_article_element = soup.find("INSERT IDENTIFIER")

    text = recusive_search(root_article_element)
        
    pass



if __name__=="__main__":
    # Load up test pages
    from util.load_test_page import get_test_requests
    
    request_list = get_test_requests()

    for page in pages_list:
        grab_meta(page)