import sqlite3

# create a funciton that can update the database and commit those changes base off input
def update(db, update_query):
    """Update the designated database based on the query string"""
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(update_query)
    # log the values of the db after the update
    cursor.execute(f"SELECT * FROM {db.split('.')[0]}")
    # log the query
    with open("query_log.txt", "a") as f:
        f.write(update_query + "\n")
        for i in range(15):
            output = str(cursor.fetchone())
            f.write(output + "\n")
            print(output)
        f.write("\n")
    conn.commit()
    conn.close()
    return "Success"
