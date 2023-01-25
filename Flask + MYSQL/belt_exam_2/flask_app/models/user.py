from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re
from pprint import pprint
from flask_app.models.painting import Painting

DATABASE = 'belt_exam_2'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.paintings = []
    
    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db( query, data )

    ## ! used in user validation
    @classmethod
    def get_by_email(cls,data:dict) -> object or bool:
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    ##! get all of a user's models
    @classmethod 
    def get_user_with_models(cls, data):
        query = "SELECT * FROM users LEFT JOIN models ON models.user_id = users.id WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        pprint(results)
        user = cls(results[0])
        for result in results:
            model_data = {
                'id': result['models.id'],
                'param1': result['param1'],
                'param2': result['param2'],
                'param3': result['param3'],
                'user_id': result['user_id'],
                'created_at': result['models.created_at'],
                'updated_at': result['models.updated_at'],
            }
            user.models.append(Model(model_data))
        return user

    @staticmethod
    def validate_user(user:dict) -> bool:
        is_valid = True # ! we assume this is true
        if len(user['first_name']) < 2:
            flash("first name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("last name must be at least 3 characters.")
            is_valid = False
        if len(user['password']) < 8:
            flash("password must be at least 8 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if user['password'] != user['confirm-password']:
            flash("Passwords do not match")
            is_valid = False
        return is_valid