import urllib.request
import os
import argparse

class Downloader:
    '''
    Fetches all files from a user-specified URL

    Args:
        root_url: The base URL where each file is stored
    '''
    def __init__(self, root_url):
        self.root_url = root_url
    
    def download(self):
        for i in range(97, 123):
            url = self.root_url + str(chr(i)) + '.csv'
            print('Beginning file download with urllib2...')
            try:
                urllib.request.urlretrieve(url, f'data_sources/{str(chr(i))}.csv')
            except urllib.error.URLError:
                print("Not a valid url")

if __name__ == '__main__':
    '''
    Parse the root URL from the command line and store it
    '''
    parser = argparse.ArgumentParser(description='Checks for a user-supplied root URL')
    parser.add_argument('--root_URL', dest='root_URL', action='store', help='The base URL of the file store')
    args = parser.parse_args()
    root_url = args.root_URL

    '''
    Create a directory to store downloaded files
    '''
    directory = 'data_sources'
    cwd = os.getcwd() #gets the current working directory
    path = os.path.join(cwd, directory) #creates the new directory path
    try:
        os.mkdir(path)
        print(f'Directory {directory} created')
    except OSError:
        print(f'Failed to create {directory} directory. It may already exist')

    '''
    Instantiate a downloader object with a root URL
    '''
    downloader = Downloader(root_url)
    downloader.download() #call download