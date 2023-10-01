import sqlite3

# create a funciton that can update the database and commit those changes base off input
def update(db, update_query):
    """Update the designated database based on the query string"""
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(update_query)
    conn.commit()
    conn.close()
    return "Success"
