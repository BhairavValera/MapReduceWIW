def shuffle(user_map):
    '''
    Sorts the outputs from user_map first by user_id and then
    sorts each inidividual path string dictionary

    Args:
        user_map: map of user_ids to their respective paths
    '''
    sorted_user_map = dict(sorted(user_map.items(), key=lambda item: item[0])) #sort by user_ids
    for user_id, pathMap in sorted_user_map.items():
        sorted_pathMap = dict(sorted(pathMap.items(), key=lambda item: item[0])) #sort each path map alphabetically
        sorted_user_map[user_id] = sorted_pathMap
    return sorted_user_map