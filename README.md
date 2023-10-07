# Python data processing introduction

This is a basic introduction to data processing in python. The exmaples are based on the 
linkedin learning class (Data Ingestion With Python)
[https://www.linkedin.com/learning/data-ingestion-with-python], but with a simpler syntax 
more suitable for beginners.

Please review the python (Accumulator Pattern)[https://runestone.academy/ns/books/published/thinkcspy/Functions/TheAccumulatorPattern.html].  This pattern the foundation of all the techniques 
presented below (with the exception of the pandas module).

# Data files

The best starting point is to look at the 2 data files we want to process, taxi.csv and
taxi.jl.  They are the same dataset but in 2 different formats.  

csv stands for comma separated values where each line has a number of fields separated by 
comma, with the first line being the header.

jl stands for "json line" format, where each line in the text file is a json object.

The goal of the exercise is to calculate the average ride time (dropoff time - pickup time)
for the entire dataset.

The taxi.csv file can be downloaded directly from (https://raw.githubusercontent.com/env3d/python-data-ingestion-basics/main/taxi.csv)[https://raw.githubusercontent.com/env3d/python-data-ingestion-basics/main/taxi.csv]

The taxi.jl file can be downloaded directly from (https://raw.githubusercontent.com/env3d/python-data-ingestion-basics/main/taxi.jl)[https://raw.githubusercontent.com/env3d/python-data-ingestion-basics/main/taxi.jl]

# load_csv.py

This file contains annoated code to process taxi.csv file.  It presents 3 different
strategies: pure python, python's internal csv module, and pandas module.

# load_json.py

We use the python internal json module to parse each line of the taxi.jl file and 
calculate the average ride time.  

