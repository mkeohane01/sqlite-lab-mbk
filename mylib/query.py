"""Query the database"""

import sqlite3


def query():
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GroceryDB")
    print("Top 5 rows of the GroceryDB table:")
    # only pront top 5 rows not all rows
    for i in range(5):
        print(cursor.fetchone())
    conn.close()
    return "Success"


