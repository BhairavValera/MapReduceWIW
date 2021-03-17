# WIW_Coding_Challenge

## This is my completed coding challenge for When I Work.

Before running the map-reduce job, be sure to run

`pip install -r requirements.txt`

to install all dependencies. Note we only have one major dependency here (Pandas) but in a production setting, we could have multiple so it's best to use a `requirements.txt` file.

Next, run 

`downloader.py`

which will create a `data_sources` directory and fill it with the right `.csv` files.

Then, finally, run

`map_reduce_job.py`

to generate the result.