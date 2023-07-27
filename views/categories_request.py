import sqlite3
import json
from models import Category

def get_all_categories():
    """get categories"""
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            ct.id,
            ct.label
        FROM Categories ct
        """)

        # Initialize an empty list to hold all animal representations
        categories = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            category = Category(row['id'], row['label'])

            categories.append(category.__dict__)

    return categories

def create_category(new_category):
    """Adds a category to the database"""
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        Insert into Categories (label) values (?)
        """, (new_category['label'],))

        #  return the primary key of the last thing that got added to
        #  the database.
        id = db_cursor.lastrowid
        new_category['id'] = id

        return json.dumps(new_category)
