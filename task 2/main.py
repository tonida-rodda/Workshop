import json
import string
from flask import Flask, request
from database import database

app = Flask(__name__, template_folder='templates')
new_connection_db = database()

@app.route("/", methods = ['GET'])
def index():
    return 'Hello world'

@app.route("/register", methods = ['POST'])
def register():
    request_body = request.get_json()
    try:
        requested_mail: string = request_body.get('mail')
        requested_password: string = request_body.get('password')
        if (not requested_mail or not requested_password):
            raise
        new_connection_db.add_user_in_db(requested_mail, requested_password)
        return 'Account registered!'
    except:
        return 'Error in creation!'

@app.route("/login", methods = ['POST'])
def login():
    request_body = request.get_json()
    try:
        requested_mail: string = request_body.get('mail')
        requested_password: string = request_body.get('password')
        if (not requested_mail or not requested_password):
            raise
        new_connection_db.check_user_whit_creds(requested_mail, requested_password)
        return 'Logged in!'
    except:
        return 'Failed to log in!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)