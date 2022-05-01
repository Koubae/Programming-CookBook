# Built-in Imports
import os
from datetime import datetime
from base64 import b64encode
import base64
from io import BytesIO #Converts data from Database into bytes

# Flask
from flask import Flask, render_template, request, flash, redirect, url_for, send_file # Converst bytes into a file for downloads

# FLask SQLAlchemy, Database
from flask_sqlalchemy import SQLAlchemy


basedir = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.sqlite')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = basedir
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev'
db = SQLAlchemy(app)

# Picture table. By default the table name is filecontent
class FileContent(db.Model):

    """ 
    The first time the app runs you need to create the table. In Python
    terminal import db, Then run db.create_all()
    """
    """ ___tablename__ = 'yourchoice' """ # You can override the default table name

    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    data = db.Column(db.LargeBinary, nullable=False) 
    rendered_data = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text)
    location = db.Column(db.String(64))
    pic_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def __repr__(self):
        return f'Pic Name: {self.name} Data: {self.data} text: {self.text} created on: {self.pic_date} location: {self.location}'


# Index
@app.route('/index', methods=['GET', 'POST'])
@app.route('/')
def index():

    pics = FileContent.query.all()
    if pics: # This is because when you first run the app, if no pics in the db it will give you an error
        all_pics = pics
        if request.method == 'POST':

            flash('Upload succesful!')
            return redirect(url_for('upload'))  

        return render_template('index.html', all_pic=all_pics)
    else:
        return render_template('index.html')

# Query
@app.route('/query')
def query():

    all_pics = FileContent.query.all()
    return render_template('query.html', all_pic=all_pics)

# Render the pics
def render_picture(data):
    
    render_pic = base64.b64encode(data).decode('ascii') 
    return render_pic

# Upload
@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['inputFile']
    data = file.read()
    render_file = render_picture(data)
    text = request.form['text']
    location = request.form['location']

    newFile = FileContent(name=file.filename, data=data, rendered_data=render_file, text=text, location=location)
    db.session.add(newFile)
    db.session.commit() 
    full_name = newFile.name
    full_name = full_name.split('.')
    file_name = full_name[0]
    file_type = full_name[1]
    file_date = newFile.pic_date
    file_location = newFile.location
    file_render = newFile.rendered_data
    file_id = newFile.id
    file_text = newFile.text


    return render_template('upload.html', file_name=file_name, file_type=file_type, file_date=file_date, file_location=file_location, file_render=file_render, file_id=file_id, file_text=file_text)


# Download
@app.route('/download/<int:pic_id>')
def download(pic_id):
    file_data = FileContent.query.filter_by(id=pic_id).first()
    file_name = file_data.name
    return send_file(BytesIO(file_data.data), attachment_filename=file_name, as_attachment=True)


# Show Pic
@app.route('/pic/<int:pic_id>')
def pic(pic_id):

    get_pic = FileContent.query.filter_by(id=pic_id).first()

    return render_template('pic.html', pic=get_pic)

# Update
@app.route('/update/<int:pic_id>', methods=['GET', 'POST'])
def update(pic_id):

    pic = FileContent.query.get(pic_id)

    if request.method == 'POST':
        pic.location = request.form['location']
        pic.text = request.form['text']

        db.session.commit()
        flash(f'{pic.name} Has been updated')
        return redirect(url_for('index'))
    return render_template('update.html', pic=pic)


#Delete
@app.route('/<int:pic_id>/delete', methods=['GET', 'POST'])
def delete(pic_id):

    del_pic = FileContent.query.get(pic_id)
    if request.method == 'POST':
        form = request.form['delete']
        if form == 'Delete':
            print(del_pic.name)
            db.session.delete(del_pic)
            db.session.commit()
            flash('Picture deleted from Database')
            return redirect(url_for('index'))
    return redirect(url_for('index'))
    

if __name__ == '__main__':
    app.run(port=8000 ,debug=True)