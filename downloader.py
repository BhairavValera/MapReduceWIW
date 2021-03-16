import urllib.request
import os

class Downloader:
    def __init__(self, root_url):
        self.root_url = root_url
    
    def download(self):
        for i in range(97, 123):
            url = self.root_url + str(chr(i)) + '.csv'
            print('Beginning file download with urllib2...')
            urllib.request.urlretrieve(url, f'data_sources/{str(chr(i))}.csv')

if __name__ == '__main__':
    directory = 'data_sources'
    cwd = os.getcwd() #gets the current working directory
    path = os.path.join(cwd, directory)
    try:
        os.mkdir(path)
        print(f'Directory {directory} created')
    except OSError:
        print(f'Failed to create {directory} directory. Check premissions or it may already exist')
    root_url = 'https://public.wiwdata.com/engineering-challenge/data/' #<-- Change this if files are located elsewhere
    downloader = Downloader(root_url)
    downloader.download()