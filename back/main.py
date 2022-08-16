import json
import string
from flask import Flask, render_template,request
from flask_cors import CORS, cross_origin
from database import database

app = Flask(__name__, template_folder='templates')
cors = CORS(app, resources={r"/": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
new_connection_db = database()

@app.route("/", methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def index():
    return 'In health'

@app.route("/add", methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def add():
    request_body = request.get_json()
    try:
        print(request_body)
        requested_id: string = request_body.get('id')
        requested_input: string = request_body.get('todo')
        print(requested_input)
        new_connection_db.add_todo_in_inv(requested_id, requested_input)
    except:
        return 'Down'
    return 'In health'

@app.route("/login", methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def get_credentials():
    request_body = request.get_json()
    try:
        requested_mail: string = request_body.get('mail')
        requested_password: string = request_body.get('password')
        if (not requested_mail or not requested_password):
            raise
        creds = new_connection_db.check_if_user_exist_in_db(requested_mail, requested_password)
        return creds
    except:
        return 'False'

@app.route("/register", methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def register():
    request_body = request.get_json()
    requested_mail: string = request_body.get('mail')
    requested_password: string = request_body.get('password')
    if (not requested_mail or not requested_password):
            raise
    new_connection_db.add_user_in_db(requested_mail, requested_password)
    return 'True'

@app.route("/getdata", methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def getdata():
    request_body = request.get_json()
    print(request_body)
    try:
        requested_mail: string = request_body.get('email')
        creds = new_connection_db.check_if_user_exist_whit_mail(requested_mail)
        return creds
    except:
        return 'False'

@app.route("/gettodo", methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def gettodo():
    request_body = request.get_json()
    print(request_body, 'hello')
    try:
        requested_mail: string = request_body.get('id')
        response = new_connection_db.get_all_todo_by_user_id(requested_mail)
        print(response)
        return json.dumps(response)
    except:
        return 'False'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)