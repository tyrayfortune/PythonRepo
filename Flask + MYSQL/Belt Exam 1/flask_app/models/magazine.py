from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re


DATABASE = 'belt_exam'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Magazine:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.first_name = data['first_name']


    @classmethod
    def get_all(cls):
        query = 'SELECT magazines.*, users.first_name FROM magazines LEFT JOIN users ON users.id = magazines.user_id;'
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        magazines = []
        for magazine in results:
            magazines.append( cls(magazine) )
        return magazines



    @classmethod
    def save(cls, data ):
        query = "INSERT INTO magazines (title, description, user_id, created_at,  updated_at) VALUES ( %(title)s , %(description)s ,  %(user_id)s, NOW() , NOW() );"
        result = connectToMySQL(DATABASE).query_db( query, data )
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT magazines.*, users.first_name FROM magazines LEFT JOIN users ON users.id = magazines.user_id WHERE magazines.id = %(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        print(result)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE magazines title=%(title)s, description=%(description)s, WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod 
    def destroy(cls,data):
        query  = "DELETE FROM magazines WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)


    @staticmethod
    def validate_magazine(magazine:dict) -> bool:
        is_valid = True # ! we assume this is true
        if len(magazine['title']) < 2:
            flash("title must be at least 2 characters.")
            is_valid = False
        if len(magazine['description']) < 10:
            flash("Description  must be at least 10 characters.")
            is_valid = False
        return is_valid
