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
