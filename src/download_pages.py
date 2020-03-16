
import requests
import pickle
import os
from datetime import datetime
from util.request_tools import get_random_ua, extract_domain


def generate_headers():
    '''Build Headers with Random UA'''
    user_agent = get_random_ua()
    headers = {
        'user-agent': user_agent,
    }
    return headers

def generate_filename(url):
    '''Create a filename for the path formatted domain + datetime'''
    cwd = os.getcwd()
    domain_name = extract_domain(url)
    currdate = str(datetime.now())
    filename = os.path.join("test_data","pages", domain_name + "_" + currdate)
    filename = filename.replace(':', '_')
    return filename + ".page"

def page_download(url):
    '''Download and pickle the page'''
    # Pull out the content of the page
    response = requests.get(url, headers=generate_headers())
    outfile = generate_filename(url)
    with open(outfile, 'wb+') as pickle_file:
        pickle.dump(response, pickle_file)


if __name__=="__main__":
    # page_download("https://www.bloomberg.com/news/articles/2020-03-11/aramco-will-boost-oil-output-capacity-to-13-million-barrels-day?srnd=premium")
    # page_download("https://finance.yahoo.com/news/why-cheering-the-crash-in-oil-prices-like-trump-just-did-is-oversimplifying-the-risks-203530179.html")
    # page_download("https://news.yahoo.com/us-stocks-wall-street-set-130733239.html")