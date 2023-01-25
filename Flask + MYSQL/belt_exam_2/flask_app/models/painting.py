from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re



DATABASE = 'belt_exam_2'

class Painting:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.price = data['price']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.first_name = data['first_name']

#! CREATE
#! class method to add a painting to the DB 
    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO paintings (title, description, user_id, price) VALUES ( %(title)s, %(description)s, %(user_id)s, %(price)s);"
        return connectToMySQL(DATABASE).query_db( query, data )
        #! the return stmt returns the id as an int of the painting created

#! READ
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT paintings.*, users.first_name FROM paintings LEFT JOIN users ON users.id = paintings.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        paintings = []
        for painting in results: #! taking dicts from DB and making painting objects
            paintings.append( cls(painting) )
        return paintings

#! READ
    @classmethod
    def get_one(cls, data:dict) -> object:
        query = 'SELECT paintings.*, users.first_name FROM paintings LEFT JOIN users ON users.id =  paintings.user_id WHERE paintings.id =%(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

#! UPDATE
    @classmethod
    def update(cls, data:dict) -> object:
        query = 'UPDATE paintings SET title=%(title)s, description=%(description)s, user_id=%(user_id)s WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

#! DELETE
    @classmethod
    def destroy(cls, data:dict) -> object:
        query = 'DELETE FROM paintings WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

#! VALIDATION
    @staticmethod
    def validate_painting(painting:dict) -> bool:
        is_valid = True # ! we assume this is true
        if len(painting['title']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(painting['description']) < 10:
            flash("description must be at least 10 characters.")
            is_valid = False
        if len(painting['price']) < 1:
            flash("price should be greater then $0.")
            is_valid = False
        return is_valid