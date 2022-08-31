from flask import Flask, request
from database import Database
import bcrypt

app = Flask(__name__)
db = Database()
salt = bcrypt.gensalt()

def encrypt_password(password_to_encrypt: str) -> str:
    encoded_password = password_to_encrypt.encode()
    hashedPassword = bcrypt.hashpw(encoded_password, salt)
    return hashedPassword

def decrypt_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password, hashed_password)


@app.route("/", methods=['GET'])
def index():
    return 'Hello world'


@app.route("/register", methods=['POST'])
def register():
    try:
        email = request.json["email"]
        password = request.json['password']
    except KeyError:
        return 'Missing parameter'

    return db.create_user(email, encrypt_password(password))


@app.route("/login", methods=['POST'])
def login():
    try:
        email = request.json["email"]
        password = request.json['password']
    except KeyError:
        return 'Missing parameter'

    return db.get_user(email, encrypt_password(password))


@app.route("/add_todo", methods=['POST'])
def add_todo():
    try:
        user_id = request.json["user_id"]
        todo = request.json['todo']
    except KeyError:
        return 'Missing parameter'

    return db.add_todo(user_id, todo)


@app.route("/get_todos", methods=['GET'])
def get_todos():
    try:
        user_id = request.json["user_id"]
    except KeyError:
        return 'Missing parameter'

    return db.get_todos(user_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
