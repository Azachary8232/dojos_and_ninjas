from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos   

    @classmethod
    def create(cls,data):
        query = "INSERT INTO dojos (location) VALUES (%(location)s);"
        dojo_id = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return dojo_id
