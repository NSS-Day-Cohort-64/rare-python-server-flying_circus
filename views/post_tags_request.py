import sqlite3
import json
from models import PostTag

def get_all_post_tags():
    """Retrieve all post tags"""
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

def create_multiple_post_tags(post_body):
    """Create one or many postTags to relate a tag to a post when a post is created"""

    # Unpack the post id and the list of tag id's
    [new_post_id, tag_id_list] = post_body

    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        posted_tag_relationships = []

        for single_tag_id in tag_id_list:
            db_cursor.execute("""
            Insert into PostTags (post_id, tag_id) values (?, ?)
            """, (new_post_id, single_tag_id))

            #  retrieve the primary key of the last thing that got added to
            #  the database.
            id = db_cursor.lastrowid
            new_post_tag = {
                'id': id,
                'post_id': new_post_id,
                'tag_id': single_tag_id
            }
            posted_tag_relationships.append(new_post_tag)

        return json.dumps(posted_tag_relationships)
