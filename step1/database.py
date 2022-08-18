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
    data_user = (email, password)
    try:
      self.cursor.execute("INSERT INTO user (email, password) VALUES (%s, %s)", data_user)
      self.cnx.commit()
    except mysql.connector.Error as error:
      return error.msg
    return 'Account registered!'
