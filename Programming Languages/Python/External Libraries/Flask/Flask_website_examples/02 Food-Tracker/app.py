import os
from datetime import datetime

from flask import Flask, render_template, request, g, redirect, url_for, flash 
from sqlite3 import IntegrityError

# Application import
from database import connect_db, get_db
from query_data import *
from app_func import *



app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)

# Tear down Database
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

# Index
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    db = get_db()
    
    if request.method == 'POST':
        try:
             # Using function from query_data.py, process automatically dates    
            new_day = inject_date(request.form['date'])
            # Injecting Date as STR and not as Datetime Object
            print(new_day)
            db.execute(add_day, [new_day])
            db.commit()
        except ValueError as err:
            print(err)
            flash(f'Opps, You entered an empty date! Select a Date!')
        except IntegrityError as err:
            print(err)
            catch_day = request.form['date']
            flash(f'Opps, seems like you already add this day --> {catch_day} check better!') 
    
    # Query all days and show DESC/ASC
    cur = db.execute(query_all_days)
    results = cur.fetchall()
    # Get proccesed values from query_data.py 
    date_results = show_days(results)
    all_month = get_month(date_results)
    # Shows Month by User's selections.
    if request.args.get('search'):

        month_selected = select_month(request.args.get('search'), date_results)
        return render_template('index.html', results=month_selected, all_month=all_month)         
    
    return render_template('index.html', results=date_results, all_month=all_month)  
    
    
# View
@app.route('/view/<date>', methods=['GET', 'POST'])
def view(date):

    db = get_db()
    # Query date from DB
    cur = db.execute(get_date, [date])
    # Get 2 Results, Index[0] = Datatime Object, Index[1] = Pretty Date
    date_extracted = extract_date(cur.fetchone())

    # Commit Post into Database, need to be above Food Query in order to see that changes withou a redirect
    if request.method == 'POST':
        
        try:    
            if request.form['select'] != 'delete':
                print('form is add')
                db.execute(insert_food, [request.form['select'], date_extracted[0]])
                db.commit()
        except IntegrityError as err:
            print(err)
            flash('You can eat the same food twice')

    # Get Food list to inject as Select <option> Tags
    food_results = get_food(db)
    # Select log_date, create a relationship between log_date and food with food_date table. select 5 column from food
    log_results = food_log(db, date)
    # Cal Proteins/Carbs/Fat + sum(calories)
    totals = def_food_val(log_results)
    
    return render_template('day.html', date=date, \
                            pretty_date=date_extracted[2], \
                            food_results=food_results, \
                            log_results=log_results, \
                            totals=totals)

# Delete Day
@app.route('/delete/<date>', methods=['POST'])
def del_day(date):

    db = get_db()
    if request.method == 'POST':
        sql = 'DELETE from log_date WHERE entry_date = (?)'
        db.execute(sql, [date, ])
        db.commit()

    return redirect(url_for('index'))


# Add food 
@app.route('/food', methods=['GET', 'POST'])
def food():
    
    db = get_db()

    if request.method == 'POST':
        try:
            name = request.form['food-name']
            protein = int(request.form['protein'])
            carbohydrates = int(request.form['carbohydrates'])
            fat = int(request.form['fat'])
            
            calories = sum_calories(protein, carbohydrates, fat)
            db.execute(add_food,[name, protein, carbohydrates, fat, calories])
            db.commit()
        except IntegrityError as err:
            print(err)
            catch_name = request.form['food-name']
            flash(f'Opps, seems like you already have this food --> {catch_name} check better!')
       
    # Show Food in Database
    cur = db.execute(query_all_food)
    results = cur.fetchall()

    return render_template('add_food.html', results=results)

if __name__ == '__main__':
    app.run(port=5000, debug=True)