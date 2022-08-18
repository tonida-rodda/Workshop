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
    except:
        return 'Error in creation!'
    return 'Account registered!'

@app.route("/login", methods = ['POST'])
def login():
    request_body = request.get_json()
    try:
        requested_mail: string = request_body.get('mail')
        requested_password: string = request_body.get('password')
        if (not requested_mail or not requested_password):
            raise
        new_connection_db.check_user_whit_creds(requested_mail, requested_password)
    except:
        return 'Failed to log in!'
    return 'Logged in!'

@app.route("/add_todo", methods = ['POST'])
def add_data():
    request_body = request.get_json()
    try:
        requested_id: string = request_body.get('id')
        requested_input: string = request_body.get('todo')
        new_connection_db.add_todo_in_inv(requested_id, requested_input)
    except:
        return 'Error in creation of the todo!'
    return 'Todo created successfuly!'

@app.route("/get_todo", methods = ['GET'])
def get_todo():
    request_body = request.get_json()
    try:
        requested_mail: string = request_body.get('id')
        response = new_connection_db.get_all_todo_by_user_id(requested_mail)
    except:
        return 'Error no todo found!'
    return json.dumps(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)