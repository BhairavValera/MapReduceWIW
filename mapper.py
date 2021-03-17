import os
import pandas as pd

def _map():
    '''
    Goes through each file in data_sources/ and converts them into pandas data frames
    Each row of the data frame is accessed by its column name
    '''
    for i in range(97, 123): #iterate through a-z ascii characters
        file = f'{chr(i)}.csv'
        cwd = os.getcwd() #gets the current working directory
        path = os.path.join(cwd, 'data_sources', file)
        data = pd.read_csv(path)
        for _, row in data.iterrows():
            '''
            Writes tab delimited output to STDOUT (standard output)
            Output of this code will be what is used for the reduce step, i.e. the input for reducer.py
            '''
            print(f'{row["user_id"]} \t {row["path"]} \t {row["length"]}')

if __name__ == '__main__':
    _map()