from flask_app.config.mysqlconnection import connectToMySQL
from .model_ninja import Ninja

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos   

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (location) VALUES (%(location)s);"
        dojo_id = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return dojo_id

    @classmethod
    def get_one_with_ninjas(cls, data ):
        print(data)
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            # ninjas = [] in self dictionary
            dojo.ninjas.append( Ninja(n) )
        return dojo