from flask import Flask, render_template, request, redirect, url_for, flash
from flask_cors import CORS
from models import get_posts, create_post, delete_posts, get_post_data, update_posts

app = Flask(__name__)

CORS(app);
app.secret_key = "mysecretkey"
@app.route('/')
def index():
  posts = get_posts()
  return render_template('index2.html', posts=posts)

@app.route('/add_contact', methods=['POST'])
def add_post():
    if request.method == 'GET':
      pass  
    if request.method == 'POST':
      name = request.form.get('name')
      content = request.form.get('phone')
      featuredimage = request.form.get('email')
      images = request.form.get('age')
      if name == '' or content == "" or featuredimage == '' or images == '':
        flash('All the fields are required')
      else:
        create_post(name, content, featuredimage, images)
        flash('Contact Added successfully')
    return redirect(url_for('index'))

@app.route('/delete/<string:id>')
def remove_post(id):
  url = delete_posts(id)
  flash('Contact Removed Successfully')
  return redirect(url_for(url))

@app.route('/update/<id>', methods = ['POST'])
def update_post(id):
  if request.method == 'POST':
      name = request.form.get('name')
      phone = request.form.get('phone')
      email = request.form.get('email')
      age = request.form.get('age')
      update_posts(id, name, phone, email, age)
  flash('Contact updated successfully')
  return redirect(url_for('index'))
  

@app.route('/edit/<id>')
def get_post(id):
  data = get_post_data(id)
  return render_template('edit-contact.html', post = data)
if __name__ == '__main__':
  app.run(debug=True)