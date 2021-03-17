import sys
import os
import pandas as pd

def reduce():
    '''
    user_map maps user id to another hash table of paths
    the hash table of paths maps a path string to it's length
    every time we see a new user id, we create a new path map for it and put the current path in along with its length
    if the user id is found but the path is not, then create a new path with that length, else just increment its length accordingly
    '''
    user_map = {}
    for line in sys.stdin:
        line = line.strip()
        user_id, path, length = line.split('\t')

        #converting the user_id and lengths accordingly
        user_id = int(user_id)
        length = int(length)

        #removing white space from path
        path = path.strip()

        if user_id in user_map:
            if path in user_map[user_id]:
                user_map[user_id][path] += length
            else:
                user_map[user_id][path] = length
        else:
            user_map[user_id] = {}
            user_map[user_id][path] = length

    '''
    Sort the map such that the user ids go in ascending order.
    Also, sort the path names such that they are in alphabetical order
    '''
    sorted_user_map = dict(sorted(user_map.items(), key=lambda item: item[0]))
    result_data = pd.DataFrame.from_dict(sorted_user_map, orient='index').fillna(value=0)
    result_data = result_data.reindex(sorted(result_data.columns), axis=1)

    '''
    Write resulting pandas dataframe to CSV file
    '''
    cwd = os.getcwd() #gets the current working directory
    path = os.path.join(cwd, "result.csv") #create a path for the result file
    result_data.to_csv(path) #write file


if __name__ == '__main__':
    reduce()