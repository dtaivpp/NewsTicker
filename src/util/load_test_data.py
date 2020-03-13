import os
import pickle

def _get_test_data(path, loader):
    '''Returns a list of objects formatted
    in whatever mannter the loader function defines
    eg. return data.read()
    '''

    files = []
    
    # iterate over all test docs
    for filename in os.listdir(path):

        # only retrieve .page files
        if filename != '.tmp':
            path = os.path.join(path, filename)
            with open(path, 'rb') as openfile:
                files.append(loader(openfile))

    return files
    
def get_test_pages():
    '''Returns List of Sample Page Request Objects'''
    # Iterate pages in test_data folder
    testdir = os.path.join(os.curdir,'test_data', 'pages')
    
    def load(request):
        return pickle.load(request)

    return _get_test_data(testdir, load)
 

def get_test_text():
    '''Returns List of Sample Article Texts'''
    # Iterate pages in test_data folder
    testdir = os.path.join(os.curdir,'test_data', 'text')
    
    def load(file):
        return file.read() 
    
    return _get_test_data(testdir, load)


if __name__ == "__main__":
    page = get_test_pages()
    print(page)