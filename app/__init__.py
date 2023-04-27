from flask import Flask
from flask_sqlalchemy import SQLAlchemy
myapp_obj = Flask(__name__)
db = SQLAlchemy(myapp_obj)



from app import routes