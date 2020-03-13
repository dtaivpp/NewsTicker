from urllib.parse import urlparse

def extract_domain(url, remove_http=True):
    '''Return the domain name'''
    uri = urlparse(url)
    if remove_http:
        domain_name = f"{uri.netloc}"
    else:
        domain_name = f"{uri.netloc}://{uri.netloc}"
    return domain_name
