import sqlite3
import json
from datetime import datetime
from models import User

def login_user(user):
    """Checks for the user in the database

    Args:
        user (dict): Contains the username and password of the user trying to login

    Returns:
        json string: If the user was found will return valid boolean of True and 
        the user's id as the token If the user was not found will return valid boolean False
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            select id, username
            from Users
            where username = ?
            and password = ?
        """, (user['username'], user['password']))

        user_from_db = db_cursor.fetchone()

        if user_from_db is not None:
            response = {
                'valid': True,
                'token': user_from_db['id']
            }
        else:
            response = {
                'valid': False
            }

        return json.dumps(response)


def create_user(user):
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
        Insert into Users (first_name, last_name, email, bio, username, password, profile_image_url, created_on, active) values (?, ?, ?, ?, ?, ?, ?, ?, 1)
        """, (
            user['first_name'],
            user['last_name'],
            user['email'],
            user['bio'],
            user['username'],
            user['password'],
            user['profile_image_url'],
            datetime.now()
        ))

        id = db_cursor.lastrowid

        return json.dumps({
            'token': id,
            'valid': True
        })


def get_all_users():
    """Retrieve all users"""
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        FROM Users u
        """)

        # Initialize an empty list to hold all animal representations
        users = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            user = User(row['id'], row['first_name'], row['last_name'],
                            row['email'], row['bio'],
                            row['username'], row['password'], row['profile_image_url'],
                           row['created_on'], row['active'])

            users.append(user.__dict__)

    return users


def get_single_user(id):
    """Get single item"""
    with sqlite3.connect("./db.sqlite3") as conn:

        # Initialize the cursor object and access rows by column name
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Default value for result
        requested_user = None

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        FROM Users u
        WHERE u.id = ?
        """, ( id, ))

        # Convert single row of data into a Python list
        data = db_cursor.fetchone()

        # Check if the selected item exists
        if data is not None:
            user = User(data['id'], data['first_name'], data['last_name'],
                                data['email'], data['bio'],
                                data['username'], data['password'], data['profile_image_url'],
                            data['created_on'], data['active'])
            requested_user = user.__dict__

    return requested_user
