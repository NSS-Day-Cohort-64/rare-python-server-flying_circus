import sqlite3
import json
from datetime import datetime
from models import PostTag

def get_all_post_tags():
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            pt.id,
            pt.post_id,
            pt.tag_id
        FROM PostTags pt
        """)
        # Initialize an empty list to hold all animal representations
        post_tags = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            post_tag = PostTag(row['id'], row['post_id'], row['tag_id'] )

            post_tags.append(post_tag.__dict__)

    return post_tags


