import os
import pickle

def get_test_requests():
    '''Returns a list of response objects'''

    # Iterate pages in test_data folder
    testdir = os.path.join(os.curdir,'test_data')
    request_files = []
    
    # iterate over all test docs
    for filename in os.listdir(testdir):
        file_parts = os.path.splitext(filename)

        # only retrieve .page files
        if file_parts[len(file_parts)-1] == '.page':
            path = os.path.join(testdir, filename)
            with open(path, 'rb') as openfile:
                request = pickle.load(openfile)
                request_files.append(request)

    return request_files

if __name__ == "__main__":
    pass