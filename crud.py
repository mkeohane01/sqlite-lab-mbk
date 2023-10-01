"""
ETL-Query script
"""
import fire
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query
from mylib.update import update

# by defualt loading baseball data but can specify any url, file path, or db name
default_url = "https://raw.githubusercontent.com/datacamp/courses-introduction-to-python/master/datasets/baseball.csv"
default_file_path = "data/baseball_data.csv"
default_db_name = "BaseballDB"
default_query_str = f"SELECT * FROM {default_db_name}"
default_update_query = \
    f"UPDATE {default_db_name} SET Weight = WEIGHT * 2 WHERE Team = 'CHC'"
default_delete_query = f"DELETE FROM {default_db_name} WHERE Team = 'CHC'"

class CRUD():
    ''' Class containing functions to 
      1.create a sqlite3 database
      2.read the database through queries
      3.update the database based on query
      4.delete parts of the database based on query'''
    
    # create a databse based on the url, file path, and db name
    def create(self, url=default_url, file_path=default_file_path, db_name=default_db_name):
        # Create
        # Inputs: url, file_path, db_name
        print(f"Creating database...{db_name}")
        extract(url, file_path)
        load(file_path, db_name)

    # read the database and print the resulting query
    def read(self, db=f"{default_db_name}.db", query_str=default_query_str, n_prints=5):
        # Query
        # Inputs: db, query, n_prints
        print("Querying data...")
        query(db, query_str, n_prints)
    
    # update the data based on the query
    def update(self, db=f"{default_db_name}.db", update_query=default_update_query):
        # Update
        # Inputs: db, query
        print(f"Updating data... \n based on: {update_query}")
        update(db, update_query)

    # delete parts of the database based on the query
    def delete(self, db=f"{default_db_name}.db", del_query=default_delete_query):
        # Delete
        # Inputs: db, query
        print(f"Deleting data... \n based on: {del_query}")
        update(db, del_query)

if __name__ == "__main__":
    fire.Fire(CRUD)