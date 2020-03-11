from bs4 import BeautifulSoup
import lxml

valid_descendants = {'p', 'li', 'td', 'a'}

def recusive_search(root_element):
    for descendent in root_element.descendants:
        if descendent.name in valid_descendants:
            # Need a better way to isolate releated elements? 
            # Possibly a specific scrape per site? 
            print(descendent.text)


def page_processer(path, *article_identifier):
    # Pull out the content of the page
    soup = BeautifulSoup(response.text, 'lxml')
    unwanted = soup.findAll("aside")
    if (unwanted != None and len(unwanted) > 0 ):
        unwanted.extract()
    root_article_element = soup.find(article_identifier)
    
    text = recusive_search(root_article_element)
        
    pass



if __name__=="__main__":
    # Iterate pages in test_data folder
    pass