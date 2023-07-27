import sqlite3
import json
from datetime import datetime
from models import Post

def get_all_posts():
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM Posts p
        ORDER BY p.publication_date DESC
        """)

        # Initialize an empty list to hold all animal representations
        posts = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            post = Post(row['id'],row['user_id'], 
                        row['category_id'], row['title'], 
                        row['publication_date'],row['image_url'], 
                        row['content'], row['approved'])

            posts.append(post.__dict__)

    return posts

def get_single_post(id):
    """Get single item"""
    with sqlite3.connect("./db.sqlite3") as conn:

        # Initialize the cursor object and access rows by column name
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Default value for result
        requested_post = None

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM Posts p
        WHERE p.id = ?
        """, ( id, ))

        # Convert single row of data into a Python list
        data = db_cursor.fetchone()

        # Check if the selected item exists
        if data is not None:
            post = Post(data['id'],data['user_id'],
                        data['category_id'], data['title'],
                        data['publication_date'],data['image_url'],
                        data['content'], data['approved'])
            requested_post = post.__dict__

    return requested_post
