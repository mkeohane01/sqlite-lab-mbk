"""Query the database"""

import sqlite3


def query(db="BaseballDB.db", query="SELECT * FROM BaseballDB", n_prints=5):
    """Query the designated database based on the query string"""
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(query)
    for i in range(n_prints):
        print(cursor.fetchone())
    conn.close()
    return "Success"


