"""
Transforms and Loads data into the local SQLite3 database

"""
import sqlite3
import csv
import os

#load the csv file and insert into a new sqlite3 database
def load(dataset="data/baseball_data.csv", db_name="BaseballDB"):
    """"Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    header = next(payload)
    # connect to the database
    conn = sqlite3.connect(f"{db_name}.db")
    c = conn.cursor()
    # drop the table if it already exists
    c.execute(f"DROP TABLE IF EXISTS {db_name}")
    # create the table using the header from the csv reader
    c.execute(f"CREATE TABLE {db_name} ({','.join(header)})")
    # make the ?s align with number of columns
    question_marks = ["?"] * len(header)
    question_marks = ",".join(question_marks)
    # insert the data into the table
    c.executemany(f"INSERT INTO {db_name} VALUES ({question_marks})", payload)
    conn.commit()
    conn.close()
    return f"{db_name}.db"

