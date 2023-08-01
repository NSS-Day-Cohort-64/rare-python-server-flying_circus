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

        # Get posts from subscribed authors if follower_id is provided
        if follower_id:
            db_cursor.execute("""
            SELECT DISTINCT
                p.id,
                s.author_id,
                u.username AS author_username,
                p.image_url,
                p.publication_date,
                p.title,
                ct.label AS category_label
            FROM Subscriptions s
            JOIN Users u ON s.author_id = u.id
            JOIN Posts p ON u.id = p.user_id
            JOIN Categories ct ON p.category_id = ct.id
            WHERE s.follower_id = ?
            """, (follower_id,))

        dataset = db_cursor.fetchall()

        homepage_content = []
        for row in dataset:
            subscription_data = {
                'id': row['id'],
                'author_id': row['author_id'],
                'author_username': row['author_username'],
                'image_url': row['image_url'],
                'publication_date': row['publication_date'],
                'title': row['title'],
                'category_label': row['category_label']
            }
            homepage_content.append(subscription_data)

        if len(homepage_content) == 0:
            homepage_content = {
                    'message': "Subscribe to authors to curate your personal homepage"
                }

        
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


def delete_subscription(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Subscriptions
        WHERE id = ?
        """, (id, ))
