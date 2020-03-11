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


def page_processer(path, *article_identifier):
    # Pull out the content of the page
    with open(path, 'rb') as openfile:
        response = pickle.load(openfile)

        soup = BeautifulSoup(response.text, 'lxml')
        
        root_article_element = soup.find(article_identifier)
    
        text = recusive_search(root_article_element)
        
    pass



if __name__=="__main__":
    # Iterate pages in test_data folder
    testdir = os.path.join(os.curdir,'test_data')
    
    # iterate over all test docs
    for filename in os.listdir(testdir):
        file_parts = os.path.splitext(filename)

        # only retrieve .page files
        if file_parts[len(file_parts)-1] == '.page':
            page_processer(os.path.join(testdir, filename), 'article')
    