import os
import csv

def reduce(user_map):
    result_dir = os.getcwd()
    file_path = os.path.join(result_dir, 'result.csv')
    with open(file_path, 'w') as csv_file:
        headers = [field for field, _ in list(user_map.items())[0][1].items()] #getting all path names
        headers.insert(0, 'user_id')
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for user_id, fields in user_map.items():
            row = {}
            row['user_id'] = user_id
            row = {**row, **fields} #merge dictionaries
            writer.writerow(row)