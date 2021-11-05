# This is where classes go (class User, @classmethod)

from flask_app.config.mysqlconnection import connectToMySQL

class (User)/no():
    def __init__(self,data):
        self.id = data['id']

@classmethod
def get_all(cls):
    query = "SELECT * FROM (users)/no());"
    (userS/no()) = connectToMySQL('*userS*').query_db(query)
    (users/no()) = []
    for user in (userS/no()):
        (userS/no()).append(cls(user))
    return (userS/no())   

@classmethod
def create(cls,data):
    query = "INSERT INTO (users/no()) (*something*, *something*) VALUES (%(*something*)s, %(*something*)s;"
    (user/no())_id = connectToMySQL('(userS/no())').query_db(query,data)
    return (user/no())_id
