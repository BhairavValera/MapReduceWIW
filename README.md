# WIW_Coding_Challenge

## This is my completed coding challenge for When I Work.

### Step 1
Be sure to run

`pip install -r requirements.txt`

to install all dependencies. Note we only have one major dependency here (Pandas) but in a production setting, we could have multiple so it's best to use a `requirements.txt` file.

### Step 2
Run

`python3 downloader.py --root_URL <URL>`

which will create a `data_sources` directory and fill it with the right `.csv` files. It will catch invalid URLs.

### Step 3
To run the map-shuffle-reduce job which will create the output `result.csv` file, run

`python3 mapper.py | sort -k1,1 | python3 reducer.py`

`|` will pipe the standard output of the command preceding it to the next command as input. 
`result.csv` is the file which contains per-user format data i.e. each row is a different user and the columns represent the time spent on each of the pages.
