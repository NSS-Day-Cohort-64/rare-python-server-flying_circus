import sqlite3
import json
from datetime import datetime
from models import Reaction

def get_all_reactions():
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            r.id,
            r.label,
            r.image_url
        FROM Reactions r
        """)

        # Initialize an empty list to hold all animal representations
        reactions = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            reaction = Reaction(row['id'], row['label'], row['image_url'] )

            reactions.append(reaction.__dict__)

    return reactions



