import os
import csv
import string

def map(user_map):
    '''
    Creates a map of the user_ids to their respective paths and lengths

    Args:
        user_map: Empty user_map to be filled
        user_map maps user id to another hash table of paths
        the hash table of paths maps a path string to its length
        every time we see a new user id, we create a new path map for it and put the current path in along with its length
        if the user id is found but the path is not, then create a new path with that length, 
        else just increment its length accordingly
    '''

    '''
    Go through each data file and map accordingly
    '''
    cwd = os.getcwd() #gets the current working directory
    path = os.path.join(cwd, 'data_sources')
    unique_paths = set() #keep a set of webpaths to fill in later
    for c in string.ascii_lowercase:
        file = os.path.join(path, f'{c}.csv')
        with open(file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader) #skip first row (data labels)
            for row in reader:
                # accessing data and converting
                user_id = int(row[4])
                webpath = row[2]
                length = int(row[1])

                if webpath not in unique_paths:
                    unique_paths.add(webpath)

                # mapping
                if user_id in user_map:
                    if webpath in user_map[user_id]:
                        user_map[user_id][webpath] += length
                    else:
                        user_map[user_id][webpath] = length
                else:
                    user_map[user_id] = {}
                    user_map[user_id][webpath] = length
    '''
    If a particular user never visited a path, set the length of that path to 0 
    '''
    for _, value in user_map.items():
        for webpath in unique_paths:
            if webpath not in value:
                value[webpath] = 0