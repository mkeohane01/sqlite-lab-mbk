"""Query the database"""

import sqlite3


def query(db="BaseballDB.db", query="SELECT * FROM BaseballDB", n_prints=5):
    """Query the designated database based on the query string"""
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(query)
    with open("query_log.txt", "a") as f:
        f.write(query + "\n")
        for i in range(n_prints):
            output = str(cursor.fetchone())
            f.write(output + "\n")
            print(output)
        f.write("\n")
    conn.close()
    return "Success"


