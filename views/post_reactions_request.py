import sqlite3
import json
from datetime import datetime
from models import PostReaction

def get_all_post_reactions():
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            pr.id,
            pr.user_id,
            pr.reaction_id,
            pr.post_id
        FROM PostReactions pr
        """)

        # Initialize an empty list to hold all animal representations
        post_reactions = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            post_reaction = PostReaction(row['id'], row['user_id'], row['reaction_id'], row['post_id'])

            post_reactions.append(post_reaction.__dict__)

    return post_reactions

