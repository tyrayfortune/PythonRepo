from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re
from flask_app.models.recipe import Recipe

DATABASE = 'recipes'
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
        self.recipes = []

    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db( query, data )

    # get all of a user's recipes
    @classmethod
    def get_users_with_recipes(cls, data):
        query = "SELECT * FROM users LEFT JOIN recipes ON recipes.user_id = users.id WHERE users.id = %(id)s;"
        results  = connectToMySQL(DATABASE).query_db(query, data)
        user = cls(results[0])
        for result in results:
            recipe_data = {
                "id": result["ninjas.id"],
                "name": result["first_name"],
                "description": result["last_name"],
                "instructions": result["age"],
                "date_made_on": result['date_made_on'],
                "under_30_minutes": result['under_30_minutes'],
                "user_id": result['user_id'],
                "created_at": result["recipes.created_at"],
                "updated_at": result["recipes.updated_at"]
            }
            user.recipes.append(Recipe(recipe_data))
        return user

       ## ! used in user validation
    @classmethod
    def get_by_email(cls,data:dict) -> object or bool:
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @staticmethod
    def validate_user(user:dict) -> bool:
        is_valid = True # ! we assume this is true
        if len(user['first_name']) < 3:
            flash("First name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last name must be at least 3 characters.")
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