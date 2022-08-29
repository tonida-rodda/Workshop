from array import array
from sqlite3 import Cursor
import string
import mysql.connector

class database:

  config = {
    'user': 'root',
    'password': 'new-password',
    'host': '127.0.0.1',
    'database': 'user_account',
  }
  cnx = mysql.connector.connect(**config)    
  cursor = cnx.cursor()

  add_user = ("INSERT INTO User "
               "(Email, Password) "
               "VALUES (%s, %s)")

  check_user = ("SELECT Id FROM User WHERE Email = %s AND Password = %s")

  add_todo = ("INSERT INTO invent (user_id, todo) VALUES (%s, %s)")

  get_todo = ("SELECT todo FROM invent WHERE user_id = %s")

  def __init__(self) -> None:
    pass

  def add_user_in_db(self, email: string, password: string):
    data_user = (email, password)
    self.cursor.execute(self.add_user, data_user)
    self.cnx.commit()
  
  def get_user_whit_creds(self, email: string, password: string):
    creds = (email, password)
    self.cursor.execute(self.check_user, creds)
    myresult = self.cursor.fetchall()
    return myresult

  def add_todo_in_inv(self, id:string, input: string):
    data_user = (id, input)
    self.cursor.execute(self.add_todo, data_user)
    self.cnx.commit()

  def get_all_todo_by_user_id(self, id:string):
    creds = id
    self.cursor.execute(self.get_todo, (creds, ))
    myresult = self.cursor.fetchall()
    return myresult