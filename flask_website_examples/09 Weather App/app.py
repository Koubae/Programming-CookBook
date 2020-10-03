import os
import os.path as op
import requests

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['DATABASE_FILE'] = 'data.sqlite'
basedir = op.join(op.abspath(op.dirname(__file__)), app.config['DATABASE_FILE'])

app.config['SECRET_KEY'] = os.urandom(16)
app.config['SQLALCHEMY_DATABASE_URI']   = 'sqlite:///' + basedir
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class City(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


@app.route('/')
def index_get():

    cities = City.query.all()
    weather_data = []

    for city in cities:
        r = get_weather_data(city.name)
        weather = {
            'id': city.id,
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        
        weather_data.append(weather)
    return render_template('weather.html', weather_data=weather_data)


@app.route('/', methods=['POST'])
def index_post():

    new_city = request.form.get('city')
    err_msg = ''

    if new_city:
        old_city = City.query.filter_by(name=new_city).first()

        if not old_city:
            r = get_weather_data(new_city)
            if r['cod'] == 200:
                new_city_obj = City(name=new_city)

                db.session.add(new_city_obj)
                db.session.commit()
            else:
                err_msg = 'That city don\'t exists.'
        else:
            err_msg = 'You tried entering a city that already exists'
    
    if err_msg:
        flash(err_msg, 'error')
    else:
        flash('City added succesfully!', 'success')
    
    return redirect(url_for('index_get'))


@app.route('/delete/<int:city_id>')
def delete_city(city_id):

    city = City.query.filter_by(id=city_id).first()
    db.session.delete(city)
    db.session.commit()
    flash(f'Deleted {city.name}', 'error')
    return redirect(url_for('index_get'))


def get_weather_data(city):

    url = f'http://api.openweathermap.org/data/2.5/weather?q={ city }&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    r = requests.get(url).json()

    return r

if __name__ == '__main__':
    if not os.path.exists(basedir):
        print('==='*15)
        print('>>> Creating Database... ---> Database Created!')
        db.create_all()
        print('==='*15)
    app.run(debug=True)