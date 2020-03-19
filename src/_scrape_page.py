from bs4 import BeautifulSoup
import lxml
from util.load_scrape_config import get_scrape_config
from util.request_tools import extract_domain

# --------------------------------------------------
# WIP New Page Scraping File Will Replace scrape_page.py
# 1. Find Outer Most Element
# 2. Locate wanted inner elements
# 3. Remove unwanted elements
# 4. Extract article text
#
# Extraction Model:
#  {
#   root_element: ["tag", {"attribute": "attribute-value"}],
#   unwanted_elements: [
    #                   ["tag", {"attribute": "attribute-value"}],
    #                   ["tag", {"attribute": "attribute-value"}]
    #                  ],
#   inner_elements:[
#                   ["tag", {"attribute": "attribute-value"}],
#                   ["tag", {"attribute": "attribute-value"}]
#                  ],
#   text_elements: [
#                   ["tag", {"attribute": "attribute-value"}],
#                   ["tag", {"attribute": "attribute-value"}]
#                  ]
#   }
# --------------------------------------------------

# Get outer element
def outer_element(page, identifyer):
    root = page.find(*identifyer)
    
    if root == None:
        raise Exception("Could not find root element")

    return root

# Remove unwanted elements
def trim_unwanted_elements(page, identifier_list):
    # Check if list has elements
    if len(identifier_list) != 0:
        for identifyer in identifier_list:
            for element in page.find_all(*identifyer):
                element.decompose()
    
    # Dont ask why I am doing this. 
    #   I know this doesnt actually
    #   do anything as I am referencing
    #   the page object...
    return page

# Get inner elements
""" def get_inner_elements(page, identifier_list):
    # Check if list has elements
    if len(identifier_list) != 0:
        for identifyer in identifier_list:
            for element in page.find_all(*identifyer)
                element.decompose()
        
    # IT MAKES ME FEEL GOOD
    return page
 """

# Extract text
def get_text(page, identifier_list):
    # Check if list has elements
    if len(identifier_list) == 0:
        raise Exception("Get text needs to know which elements to extract.")

    page_text = []
    for identifyer in identifier_list:
        for element in page.find_all(*identifyer):
            page.append(element.text)
    
    return page_text


# Get page config
def load_scrape_config():
    '''Loads page scraping config data'''
    return get_scrape_config()


def get_site_config(url):
    '''Get the scrap config for the site'''
    domain = extract_domain(url)

    config_data = load_scrape_config()
    
    config = config_data.get(domain, None)
    
    if config == None:
        raise Exception(f"Config does not exist for domiain: {domain}")
    
    return config

# Build Soup
def page_processer(request):
    '''Returns Article Text'''

    # Get the page scrape config
    site_config = get_site_config(request.url)

    # Soupify page
    soup = BeautifulSoup(request.text, 'lxml')
    
    # Retrieve root element
    root = outer_element(soup, site_config["root_element"])

    trimmed_tree = trim_unwanted_elements(root, site_config["unwanted_elements"])

    text = get_text(trimmed_tree, site_config["text_elements"])
        
    return " ".join(text)


if __name__=="__main__":
    # Load up test pages
    from util.load_test_data import get_test_pages
    
    request_list = get_test_pages()

    for page in request_list:
        text = page_processer(page)
        print(text)