

from flask_bcrypt import Bcrypt
from flask import Flask, flash
import re, PIL

app = Flask(__name__)

app.secret_key = "shhhhhh"