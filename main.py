"""
ETL-Query script
"""
import fire
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query

# initialize a class to contain CRUD functions
# by defualt loading baseball data but can specify any url, file path, or db name
def main():
    # Extract
    # Inputs: url, file_path
    print("Extracting data...")
    extract()

    # Transform and load
    # Inputs: file_path, db_name
    print("Transforming data...")
    load()

    # Query
    # Inputs: db, query, n_prints
    print("Querying data...")
    query()

if __name__ == "__main__":
    fire.Fire(main())