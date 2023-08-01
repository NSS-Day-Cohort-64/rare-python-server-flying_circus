import sqlite3
import json
from datetime import datetime
from models import Comment, User

def get_all_comments():
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content
        FROM Comments c
        """)

        # Initialize an empty list to hold all animal representations
        comments = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            comment = Comment(row['id'], row['post_id'], row['author_id'], row['content'])

            comments.append(comment.__dict__)

    return comments


def create_comment(comment):
    """Adds a user to the database when they register

    Args:
        user (dictionary): The dictionary passed to the register post request

    Returns:
        json string: Contains the token of the newly created user
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        Insert into Comments (post_id, author_id, content) values (?, ?, ?)
        """, (
            comment['post_id'],
            comment['author_id'],
            comment['content'],
        ))

        id = db_cursor.lastrowid

        return json.dumps({
            'token': id,
            'valid': True
        })

def get_comments_by_post(post_id):
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            c.id,
            c.post_id,
            c.author_id,
            c.content,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        FROM Comments c
        JOIN Users u 
        ON u.id = c.author_id
        WHERE c.post_id = ?
        """, (post_id, ))

        comments = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            comment = Comment(row['id'], row['post_id'], 
                            row['author_id'], row['content'])
            user = User(row['author_id'], row['first_name'], row['last_name'], 
                        row['email'], row['bio'], row['username'], row['password'],
                        row['profile_image_url'], row['created_on'], row['active'])

            comment.user = user.__dict__

            comments.append(comment.__dict__)
        
        return comments
    
def create_comment(new_comment):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Comments
            ( post_id, author_id, content )
        VALUES
            ( ?, ?, ? );
        """, (new_comment['post_id'], new_comment['author_id'],
             new_comment['content'] ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the snake dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_comment['id'] = id


    return json.dumps(new_comment)
