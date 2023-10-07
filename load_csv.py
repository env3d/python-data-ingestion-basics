# This example is a simpler version of the problem presented in 
# https://www.linkedin.com/learning/data-ingestion-with-python/working-in-csv

import pandas
import csv
from datetime import datetime, timedelta

def process_py():
    """
    In this first example, we are using the pure python way to calculate
    the average ride duration of taxi.csv

    This is very similar to exercises in COMP115
    """
    f = open('taxi.csv', 'r')
    # read the header line (we do this to skip the header line)
    header = f.readline().rstrip().split(',')

    # Now we process the data file  
    # We start with a variable to 
    # keep track of the total time difference
    total_time = timedelta()

    # to calculate average, we also need to keep 
    # track of the number of total lines
    num_rows = 0

    # Applying the "accumulator pattern"
    for line in f:        
        # split is a simple way to read csv files
        fields = line.rstrip().split(',')

        # need to convert fields into date and time
        pickup = datetime.fromisoformat(fields[1])
        dropoff = datetime.fromisoformat(fields[2])

        # update accumulator 
        total_time += dropoff-pickup
        num_rows += 1

    # remember to close the file object
    f.close()
    # return the average
    return total_time/num_rows


def process_csv():
    """
    This function make use of python's internal csv module
    The module documentation is here: https://docs.python.org/3/library/csv.html

    Noticed that the csv module is doing lots of work for us so we ended
    up writing less code.
    """
    f = open('taxi.csv', 'r')

    # We supply the file object into a reader to parse the csv file
    reader = csv.DictReader(f)

    # initialize some accumulator variables
    total = timedelta()
    count = 0

    # The main loop
    for record in reader:
        # each item in reader is a row in the csv file converted to a python dictionary
        delta = datetime.fromisoformat(record['tpep_dropoff_datetime']) - datetime.fromisoformat(record['tpep_pickup_datetime'])
        total += delta
        count += 1

    # remember to close the file object
    f.close()
    return total/count

def process_pandas():
    """ 
    In this function, we ingest taxi.csv file using the Pandas library
    If you are running this on your own server, you will need to install pandas 
    as follows:

        sudo pip install pandas

    The Pandas documentation is found at https://pandas.pydata.org/docs/reference/index.html
    """

    # the read_csv() function in the pandas module allows us
    # to read a csv file and returns a Dataframe object.  
    # You can then call methods of the Dataframe object to perform various calculations 
    # Noticed how on initial import, we need to tell pandas the date columns
    df = pandas.read_csv('taxi.csv', parse_dates=['tpep_pickup_datetime','tpep_dropoff_datetime'])

    # DataFrame objects have lots of features.  For example, you can 
    # perform calculations on columns.
    df['duration'] = df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']

    # We can also perform calculcations on a single column
    delta = df['duration'].mean()

    # We are returning the timedelta
    return delta

# Anything under this if statement will be executed when
# this script is called from the command line
if __name__ == '__main__':
    print(process_py())
    print(process_pandas())
    print(process_csv())