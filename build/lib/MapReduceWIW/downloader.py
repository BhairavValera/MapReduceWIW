import urllib.request
import os
import string
import sys

class Downloader:
    '''
    Fetches all files from a user-specified URL

    Args:
        root_url: The base URL where each file is stored
    '''
    def __init__(self, root_url):
        self.root_url = root_url
    
    def download(self):
        print('Beginning file downloads with urllib2...')
        cwd = os.getcwd() #gets the current working directory
        for c in string.ascii_lowercase:
            url = self.root_url + c + '.csv'
            try:
                file_save_path = os.path.join(cwd, f'data_sources/{c}.csv') #sets the path where file will be saved
                urllib.request.urlretrieve(url, file_save_path)
            except urllib.error.URLError as error:
                print(f"Root url {self.root_url} is invalid or file url is invalid. Exiting...") 
                return error
        print("Done.")