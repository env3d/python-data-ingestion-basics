# This is a simpler version of the example from 
# https://www.linkedin.com/learning/data-ingestion-with-python/json 
# 


import json
import datetime
import pandas

def process_json():
    """ 
    This function shows how to use the built-in json module to read json objects
    json objects are very similar to python dictionaries.  
    2 functions that are most important:

       json.loads( json_string ) - recevies a JSON string as input and returns python dictionary
       json.dumps( python_object ) - receives a python object and returns a JSON string

       Reference: https://docs.python.org/3/library/json.html
    """
    with open('taxi.jsonl') as f:
        sum = datetime.timedelta()
        count = 0
        for line in f:
            rec = json.loads(line)
            delta = datetime.datetime.fromisoformat(rec['dropoff'][:-1]) - datetime.datetime.fromisoformat(rec['pickup'][:-1])
            sum += delta
            count += 1

        return sum/count

def process_pandas():
    """
    Here's the equivalent solution using the pandas library.

    Important reference: https://pandas.pydata.org/docs/reference/io.html#json 
    """
    df = pandas.read_json('taxi.jsonl', lines=True, convert_dates=['pickup', 'dropoff'])
    df['duration'] = df['dropoff'] - df['pickup']
    return df['duration'].mean()
    
    
if __name__ == '__main__':
    print(process_json())
    print(process_pandas())
