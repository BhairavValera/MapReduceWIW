import os
import shutil
import argparse
import time
from . import downloader, mapper, shuffler, reducer

def main():
    '''
    Parse command line arguments
    '''
    parser = argparse.ArgumentParser(description='MapReduce package for WIW data stored at a specific root URL')
    parser.add_argument('--root_URL', dest='root_URL', action='store', help='The base URL of the file store', required=True)
    args = parser.parse_args()
    root_url = args.root_URL

    '''
    Create a temporary cache to store downloaded files
    '''
    directory = 'data_sources'
    cwd = os.getcwd() #gets the current working directory
    path = os.path.join(cwd, directory) #creates the new directory path
    try:
        print(f'Creating temporary file store...')
        os.mkdir(path)
        time.sleep(1)
        print(f'Done.')
    except OSError:
        print(f'Failed to create {directory} directory. It may already exist. Skipping this step...')

    downloader_ = downloader.Downloader(root_url) #instantiate data downloader object
    downloader_.download() #call download

    '''
    Run map-shuffle-reduce job
    '''
    print(f'Running map-shuffle-reduce job...')
    user_map = {}
    mapper.map(user_map) #map
    user_map = shuffler.shuffle(user_map)
    reducer.reduce(user_map) #reduce
    time.sleep(1)
    print(f'Done.')

    '''
    Clear the temporary file cache and remove the directory
    '''
    try:
        print(f'Cleaning up file store...')
        shutil.rmtree(path)
        time.sleep(1)
        print('Done.')
    except OSError as error:
        print(error)

if __name__ == '__main__':
    main()