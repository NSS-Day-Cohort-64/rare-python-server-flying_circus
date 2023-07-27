import sqlite3
import json
from datetime import datetime
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
        ORDER BY label ASC
        """)

        tags = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        for row in dataset:

            tag = Tag(row['id'], row['label'])

            tags.append(tag.__dict__)

    return tags