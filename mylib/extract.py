"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

by default loading a baseball dataset
"""
import requests

def extract(url="https://raw.githubusercontent.com/datacamp/courses-introduction-to-python/master/datasets/baseball.csv", 
            file_path="data/baseball_data.csv"):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path



