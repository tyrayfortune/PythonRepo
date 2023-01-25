from flask_app import app, Bcrypt
from flask_app.controllers import users, contents


if __name__ == "__main__":
    app.run(debug=True)