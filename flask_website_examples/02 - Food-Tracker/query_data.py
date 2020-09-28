from datetime import datetime


'''
Query_data.py is meant to have The SQLite3 database queries and executions
Also proccess some data from a query and returns the values like show_days function.
This is in order to keep app.py cleaner and more readable
'''



# Add a new food
add_food = 'insert into food(name, protein, carbohydrates, fat, calories) values (?,?,?,?,?)' 

# Shows all days into index.html choose whether is DESC or ASC
query_all_days = '''select log_date.entry_date,
    sum(food.protein) as protein,
    sum(food.carbohydrates) as carbohydrates,
    sum(food.fat) as fat,
    sum(food.calories) as calories 
    from log_date
    left join food_date on food_date.log_date_id = log_date.id
    left join food on food.id = food_date.food_id
    group by log_date.id order by log_date.entry_date DESC'''

query_all_month = '''select log_date.entry_date,
    sum(food.protein) as protein,
    sum(food.carbohydrates) as carbohydrates,
    sum(food.fat) as fat,
    sum(food.calories) as calories 
    from log_date
    left join food_date on food_date.log_date_id = log_date.id
    left join food on food.id = food_date.food_id
    WHERE entry_date = (?)
    group by log_date.id order by log_date.entry_date DESC '''

# Show Food
query_all_food = 'select name, protein, carbohydrates, fat, calories from food'


# Add a new day to keep track of food eaten
add_day = 'insert into log_date (entry_date) values (?)'

def inject_date(date):
    # Process argument into datetime Object
    dt = datetime.strptime(date, '%Y-%m-%d')
    # Turns datetime object into a string --> Injects into DB
    inject_date_db = datetime.strftime(dt, '%Y-%m-%d')
    print(inject_date_db)
    return inject_date_db

# Query Date from DB
get_date = 'select id, entry_date from log_date where entry_date = (?)'

def extract_date(date):

        extract_d = datetime.strptime(date['entry_date'],'%Y-%m-%d')
        pretty_date = datetime.strftime(extract_d, '%B %d, %Y') 
        check_dict = dict(date)
        if 'id' in check_dict:
            return  date['id'], extract_d, pretty_date
        return  pretty_date

# Add food into day. 
insert_food = 'insert into food_date (food_id, log_date_id) values (?,?)'

# Process Query results from 'query_all_days' and return values into a Dictionary
# The dictionary is then passed as argument to HTML index.html, and used by Jinja2
def show_days(results):

    date_results = []
    for i in results:
        single_date = {}

        single_date['entry_date'] = i['entry_date']
        single_date['protein'] = i['protein']
        single_date['carbohydrates'] = i['carbohydrates']
        single_date['fat'] = i['fat']
        single_date['calories'] = i['calories']
        # Call extrac date to proccess the date 
        single_date['pretty_date'] = extract_date(i)
        date_results.append(single_date)
 
    return date_results

# Get All food, for select + <option> in HTML
def get_food(db):

    food_cur = db.execute('select id, name from food')
    food_results = food_cur.fetchall()
    return food_results

#Query All food for adding into the Pase view 
def food_log(db, date):

    log_cur = db.execute('''select food.name, 
                                   food.protein, 
                                   food.carbohydrates, 
                                   food.fat, 
                                   food.calories
        from log_date
    join food_date on food_date.log_date_id = log_date.id
    join food on food.id = food_date.food_id
    where log_date.entry_date= (?)''', [date])

    get_log = log_cur.fetchall()
    return get_log