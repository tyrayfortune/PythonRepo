from flask_app.config.mysqlconnection import connectToMySQL
import PIL.Image as Image
import base64
from base64 import b64encode
DATABASE = 'picture_palace'

class Content:
    def __init__( self , data ):
        self.id = data['id']
        self.image = data['image']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']




    # @classmethod
    # def get_image(cls, data:dict, base64) -> object:
    #     query = 'SELECT * FROM contents where image = %(image)s;'
    #     result = connectToMySQL(DATABASE).query_db(query, data, base64)
    #     return cls(result[0])

    @classmethod
    def image_save(cls, data:dict ) -> int:
        
        query = "INSERT INTO contents (image, user_id ) VALUES ( %(image)s, %(user_id)s);"
        image = image.base64encode(data)
        return connectToMySQL(DATABASE).query_db( query, data )
        #! the return stmt returns the id as an int of the content created


#! CREATE
#! class method to add a content to the DB 
    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO contents (image, user_id ) VALUES ( %(image)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db( query, data )
        #! the return stmt returns the id as an int of the content created

#! READ
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM contents; "
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        contents = []
        for content in results: #! taking dicts from DB and making content objects
            contents.append( cls(content) )
        return contents

#! READ
    @classmethod
    def get_one(cls, data:dict) -> object:
        query = 'SELECT * FROM contents WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

#! UPDATE
    @classmethod
    def update(cls, data:dict) -> object:
        query = 'UPDATE contents SET image=%(image)s, = user_id=%(user_id)s WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

#! DELETE
    @classmethod
    def destroy(cls, data:dict) -> object:
        query = 'DELETE FROM contents WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

#! VALIDATION
    # @staticmethod
    # def validate_content(content:dict) -> bool:
    #     is_valid = True # ! we assume this is true
    #     if len(content['image']) < 5:
    #         flash("Name must be at least 3 characters.")
    #         is_valid = False
    #     if len(content['param2']) < 2:
    #         flash("Name must be at least 3 characters.")
    #         is_valid = False
    #     return is_valid