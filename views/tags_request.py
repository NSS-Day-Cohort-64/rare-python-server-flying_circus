import sqlite3
import json
from models import Tag

def get_all_tags():
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM Tags t
        ORDER BY t.label ASC
        """)

        tags = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        for row in dataset:

            tag = Tag(row['id'], row['label'])

            tags.append(tag.__dict__)

    return tags

def create_tag(new_tag):
    """Adds a tag to the database"""
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        Insert into Tags (label) values (?)
        """, (new_tag['label'],))

        #  return the primary key of the last thing that got added to
        #  the database.
        id = db_cursor.lastrowid
        new_tag['id'] = id

        return json.dumps(new_tag)
