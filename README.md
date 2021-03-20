# WIW Coding Challenge

## This is my completed coding challenge for When I Work.

### Step 1
Run

`python3 -m pip install MapReduceWIW`

to install the package. Alternatively, to install from source, run

`python3 setup.py install`

View the distribution [here](https://pypi.org/project/MapReduceWIW/). 

### Step 2
Run

`MapReduceWIW --root-url <put the URL here>`

which will run the map-shuffle-reduce job on data extracted from the root URL. After the job is completely finished, a `result.csv` file will be created in whatever directory the above command was run.

`result.csv` contains per-user format data i.e. each row is a different user and the columns represent the time spent on each of the pages.
