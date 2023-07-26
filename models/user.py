class Users():
    """ Creating new Owner!"""
    # Class initializer. It has 4 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    #All I'm doing here is setting up the Owner class so that I can use it later on in functions

    def __init__(self, id, first_name, last_name, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email