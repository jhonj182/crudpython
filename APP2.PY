  from flask import Flask, render_template, request
from flask_cors import CORS
from models import get_posts, create_post

app = Flask(__name__)

CORS(app);

@app.route('/')
def index():
  return render_template('index2.html')

@app.route('/add_contacts', methods=['GET', 'POST'])
def add_contact():
  if request.method == 'GET':
    pass  
  if request.method == 'POST':
    name = request.form.get('name')
    content = request.form.get('content')
    featuredimage = request.form.get('featuredimage')
    images = request.form.get('images')
    create_post(name, content, featuredimage, images)
  return 'Mensaje Recibido'

@app.route('/edit')
def edit_contact():
  return 'edit'

@app.route('/delete')
def delete_contact():
  return 'edit'

if __name__ == '__main__':
  app.run(port = 3000, debug=True)