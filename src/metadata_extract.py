from bs4 import BeautifulSoup
import lxml

def grab_meta(request):
    '''Create a json metadata object from request object'''
    page = request.text
    soup = BeautifulSoup(page, 'lxml')

    meta_list = soup.findAll('meta')

    metadata = {}

    for tag in meta_list:
        if "property" in tag.attrs:
            if "og:" in tag.attrs["property"]:
                metadata[tag.attrs["property"]] = tag.attrs["content"]

    return metadata

if __name__=="__main__":
    # Load up test pages
    from util.load_test_page import get_test_requests
    
    request_list = get_test_requests()

    for page in request_list:
        grab_meta(page)