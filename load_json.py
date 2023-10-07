# This is a simpler version of the example from 
# https://www.linkedin.com/learning/data-ingestion-with-python/json 
# 
# It shows how to use the basic python json module

import json
import datetime

def process_json():
    with open('taxi.jsonl') as f:
        sum = datetime.timedelta()
        count = 0
        for line in f:
            rec = json.loads(line)
            delta = datetime.datetime.fromisoformat(rec['dropoff'][:-1]) - datetime.datetime.fromisoformat(rec['pickup'][:-1])
            sum += delta
            count += 1

        return sum/count

if __name__ == '__main__':
    print(process_json())