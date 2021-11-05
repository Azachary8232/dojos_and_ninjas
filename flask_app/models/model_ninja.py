# This is where classes go (class User, @classmethod)

from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.id = data['id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas   

    @classmethod
    def create(cls,data):
        query = "INSERT INTO ninjas (*something*, *something*) VALUES (%(*something*)s, %(*something*)s;"
        ninja_id = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return ninja_id
