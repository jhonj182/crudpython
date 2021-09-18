import sqlite3 as sql
from os import path
ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, phone, email, age):
  args = '"' + name + '"'+ ','+ '"'+ phone+'"'+ ','+'"'+email+'"'+','+'"'+age+'"'
  request ='insert into posts (name, phone, email, age) values(' + args + ')'
  con = sql.connect(path.join(ROOT, 'database.db'))
  cursor = con.cursor()
  cursor.execute(request);
  con.commit()
  con.close()
  
def get_posts():
  con = sql.connect(path.join(ROOT, 'database.db'))
  cursor = con.cursor()
  cursor.execute('select * from posts')
  posts = cursor.fetchall()
  return posts

def delete_posts(id):
  con = sql.connect(path.join(ROOT, 'database.db'))
  cursor = con.cursor()
  cursor.execute('delete from posts where id = {0}'.format(id))
  con.commit()
  con.close()
  return 'index'

def get_post_data(id):
  con = sql.connect(path.join(ROOT, 'database.db'))
  cursor = con.cursor()
  cursor.execute('SELECT * FROM posts where id = {0}'.format(id))
  data = cursor.fetchall()
  con.close()
  return data[0]

def update_posts(id, name, phone, email, age):
  args = '"' + name + '"'+ ','+ '"'+ phone+'"'+ ','+'"'+email+'"'+','+'"'+age+'"'
  request ='insert into posts (name, phone, email, age) values(' + args + ')'
  con = sql.connect(path.join(ROOT, 'database.db'))
  cursor = con.cursor()
  cursor.execute("""
                 UPDATE posts
                 SET name = '{0}',
                     phone = '{1}',
                     email = '{2}',
                     age = '{3}'
                 WHERE id = {4}
                 """.format(name, phone, email, age, id))
  con.commit()
  con.close()
  return 'index'