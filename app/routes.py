import re
from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    me = {
        "first_name": "Naqui",
        "last_name": "Darby",
        "hobbies": "Basketball",
    }
    return me 