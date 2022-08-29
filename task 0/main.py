import json
import string
from flask import Flask
from database import database

app = Flask(__name__, template_folder='templates')
new_connection_db = database()

@app.route("/", methods = ['GET'])
def index():
    return 'Hello world'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)