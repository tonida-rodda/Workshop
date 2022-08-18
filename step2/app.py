from flask import Flask, request
from database import Database

app = Flask(__name__)
db = Database()


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

    return db.create_user(email, password)


@app.route("/login", methods=['POST'])
def login():
    try:
        email = request.json["email"]
        password = request.json['password']
    except KeyError:
        return 'Missing parameter'

    return db.get_user(email, password)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
