from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re


DATABASE = 'recipes'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30_minutes = data['under_30_minutes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.date_made_on = data['date_made_on']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        recipes = []
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO recipes (name, description, instructions, under_30_minutes, date_made_on , user_id, created_at,  updated_at) VALUES ( %(name)s , %(description)s , %(instructions)s ,%(under_30_minutes)s , %(date_made_on)s , %(user_id)s, NOW() , NOW() );"
        result = connectToMySQL(DATABASE).query_db( query, data )
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM recipes WHERE id = %(id)s";
        result = connectToMySQL('recipes').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE recipes name=%(name)s, description=%(description)s, instructions=%(instructions)s, under_30_minutes=%(under_30_minutes)s, date_made_on%(date_made_on)s,  WHERE id = %(id)s;"
        return connectToMySQL('recipes').query_db(query,data)

    @classmethod 
    def destroy(cls,data):
        query  = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('recipes').query_db(query,data)


    @staticmethod
    def validate_recipe(recipe:dict) -> bool:
        is_valid = True # ! we assume this is true
        if len(recipe['name']) < 3:
            flash("name must be at least 3 characters.")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Instructions name must be at least 3 characters.")
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash("description must be at least 3 characters.")
            is_valid = False
        if recipe['date_made_on'] == "":
            flash("date cannot be blank.")
            is_valid = False
        return is_valid

