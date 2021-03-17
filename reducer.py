import sys
import pandas as pd

def reduce():
    '''
    user_map is a hash table that maps user id to a hash_table of paths
    the hash table of paths maps a path to it's length
    every time we see a new user id, we create a hash_map for it and put the path in
    if the user id is found but the path is not, then create a new path with that count, ele just increment its count accordingly
    '''
    user_map = {}
    for line in sys.stdin:
        line = line.strip()
        user_id, path, length = line.split('\t')

        #converting the user_id and lengths accordingly
        user_id = int(user_id)
        length = int(length)

        if user_id in user_map:
            if path in user_map[user_id]:
                user_map[user_id][path] += length
            else:
                user_map[user_id][path] = length
        else:
            user_map[user_id] = {}
            user_map[user_id][path] = length
    for key, value in user_map.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    reduce()