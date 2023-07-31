import sqlite3
import json
from datetime import datetime
from views.posts_request import get_posts_by_user
from models import Subscription, Post

def get_all_subscriptions():
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            s.id,
            s.follower_id,
            s.author_id,
            s.created_on
        FROM Subscriptions s
        """)

        subscriptions = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:
            subscription = Subscription(row['id'], row['follower_id'], row['author_id'], row['created_on'] )

            subscriptions.append(subscription.__dict__)

    return subscriptions

def get_single_subscription(id):
    """Get single item"""
    with sqlite3.connect("./db.sqlite3") as conn:

        # Initialize the cursor object and access rows by column name
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Default value for result
        requested_subscription = None

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            s.id,
            s.follower_id,
            s.author_id,
            s.created_on
        FROM Subscriptions s
        WHERE s.id = ?
        """, ( id, ))

        # Convert single row of data into a Python list
        data = db_cursor.fetchone()

        # Check if the selected item exists
        if data is not None:
            post = Subscription(data['id'], data['follower_id'], data['author_id'], data['created_on'])
            requested_subscription = post.__dict__

    return requested_subscription

def get_homepage_content(follower_id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Get posts from subscribed authors if user_id is provided
        if follower_id:
            db_cursor.execute("""
            SELECT
                s.id,
                s.follower_id,
                u.username,
                p.image_url,
                p.publication_date,
                p.title,
                ct.label
            FROM Subscriptions s
            JOIN Posts p ON p.user_id = s.author_id, Users u ON p.user_id = u.id, Categories ct ON p.category_id = ct.id
            WHERE s.follower_id = ?
            """, (follower_id,))

        dataset = db_cursor.fetchall()

        # Convert rows of data into a Python list of dictionaries
        homepage_content = []
        for row in dataset:
            subscription_data = {
                'id': row['id'],
                'follower_id': row['follower_id'],
                'author_username': row['username'],
                'image_url': row['image_url'],
                'publication_date': row['publication_date'],
                'title': row['title'],
                'category_label': row['label']
            }
            homepage_content.append(subscription_data)

    return homepage_content



def create_subscription(new_subscription):
    """Adds a tag to the database"""
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Subscriptions
            ( follower_id, author_id, created_on )
        VALUES
            ( ?, ?, ?);
        """, (new_subscription['follower_id'], new_subscription['author_id'], new_subscription['created_on']))

        #  return the primary key of the last thing that got added to
        #  the database.
        id = db_cursor.lastrowid
        new_subscription['id'] = id

        return json.dumps(new_subscription)


