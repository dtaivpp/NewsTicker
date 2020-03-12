from bs4 import BeautifulSoup
import lxml

def grab_meta(request):
    '''Create a json metadata object from meta tags'''
    page = request.text
    soup = BeautifulSoup(page, 'lxml')

    meta_list = soup.findAll('meta')

    for tag in meta_list:
        if "og:" in tag["property"]:
            print( tag["property"] )


if __name__=="__main__":
    # Load up test pages
    from util.load_test_page import get_test_requests
    
    request_list = get_test_requests()

    for page in pages_list:
        grab_meta(page)