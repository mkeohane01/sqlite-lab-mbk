"""
Extract a dataset from a URL. 
CSV formats tend to work well

by default loading a baseball dataset
"""
import requests
default_url = \
    "https://raw.githubusercontent.com/datacamp/courses-introduction-to-python/master/datasets/baseball.csv"

def extract(url=default_url, 
            file_path="data/baseball_data.csv"):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path



