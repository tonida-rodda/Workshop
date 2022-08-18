from array import array
from sqlite3 import Cursor
import string
import mysql.connector
from mysql.connector import errorcode

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

  check_user_whit_mail = ("SELECT * FROM User WHERE Email = %s")

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

  def get_user_whit_mail(self, email: string):
    creds = email
    self.cursor.execute(self.check_user_whit_mail, (creds, ))
    myresult = self.cursor.fetchall()
    return myresult
  
  def check_user_whit_creds(self, email: string, password: string):
    creds: list = self.get_user_whit_creds(email, password)
    try:
      first_elem = creds.pop(0)
      self.id = first_elem
    except:
      return ''
    return str(first_elem[0])

  def check_if_user_exist_whit_mail(self, email: string):
    creds: list = self.get_user_whit_mail(email)
    try:
      first_elem = creds.pop(0)
      self.id = first_elem
    except:
      return ''
    return str(first_elem[0])

  def add_todo_in_inv(self, id:string, input: string):
    data_user = (id, input)
    self.cursor.execute(self.add_todo, data_user)
    self.cnx.commit()

  def get_all_todo_by_user_id(self, id:string):
    creds = id
    self.cursor.execute(self.get_todo, (creds, ))
    myresult = self.cursor.fetchall()
    return myresult