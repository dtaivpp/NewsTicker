from util.load_scrape_config import get_scrape_config
from util.request_tools import extract_domain

# --------------------------------------------------
# WIP New Page Scraping File Will Replace scrape_page.py
# 1. Find Outer Most Element
# 2. Locate wanted inner elements
# 3. Remove unwanted elements
# 4. Extract article text
# --------------------------------------------------

# Get outer element
def outer_element(page, identifyer):
    page.find()

# Remove unwanted elements

# Get inner elements

# Extract text

# Get page config
def load_scrape_config():
    '''Loads page scraping config data'''
    return get_scrape_config()


def get_site_config(url):
    '''Get the scrap config for the site'''
    domain = extract_domain(url)

    config_data = load_scrape_config()
    
    config = config.get(domain, None)
    
    if config != None:
        return config
    else: 
        raise Exception(f"Config does not exist for domiain: {domain}")


# Build Soup
def page_processer(request):
    '''Returns Article Text'''
    # Pull out the content of the page
    article_identifier = element_to_target(request.url)

    soup = BeautifulSoup(request.text, 'lxml')
    
    # Query config file for type of identifier needed
    root_article_element = soup.find(article_identifier)

    text = recusive_search(root_article_element)
        
    return text
