class User():
    """ Creating new Classs!"""
    # Class initializer. It has 12 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    #All I'm doing here is setting up the Owner class so that I can use it later on in functions

    def __init__(self, id, first_name, last_name, email, bio, username, password, profile_image_url, created_on, active):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.bio = bio
        self.username = username
        self.password = password
        self.profile_image_url = profile_image_url
        self.created_on = created_on
        self.active = active