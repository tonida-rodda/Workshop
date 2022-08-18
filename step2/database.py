import mysql.connector

class Database:

  def __init__(self) -> None:
    config = {
      'user': 'root',
      'password': 'root',
      'host': 'localhost',
      'database': 'flask-workshop-poc'
    }
    self.cnx = mysql.connector.connect(**config)
    self.cursor = self.cnx.cursor()


  def create_user(self, email: str, password: str) -> str:
    try:
      self.cursor.execute("INSERT INTO user (email, password) VALUES (%s, %s)", (email, password))
      self.cnx.commit()
      return 'Account registered!'
    except mysql.connector.Error as error:
      return error.msg


  def get_user(self, email: str, password: str) -> str:
    try:
      self.cursor.execute("SELECT id FROM user WHERE email = %s AND password = %s", (email, password))
      user = self.cursor.fetchone()
      if user is None:
        return 'User not found'
      user_id, = user
      return f"Found user with id {user_id}"
    except mysql.connector.Error as error:
      return error.msg
