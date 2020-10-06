

# Calculates the Food Calories
def def_food_val(log_results):

    totals = {'protein': 0, 'carbohydrates': 0, 'fat': 0, 'calories': 0}
    
    for food in log_results:
        totals['protein'] += food['protein']
        totals['carbohydrates'] += food['carbohydrates']
        totals['fat'] += food['fat']
        totals['calories'] += food['calories']
        
    return totals


def sum_calories(protein, carbohydrates, fat):
    
    calories = protein * 4 + carbohydrates * 4 + fat * 9
    return calories

def get_month(date):
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return month_list

# Query Month by User's selection, return the query total cleared up my the month choosen
def select_month(arg, date_results):

    new_list = []
        
    for idx, i in enumerate(date_results):
        user_selection = arg
        if user_selection in i['pretty_date']:
            y = date_results.pop(idx)
            new_list.append(y)
        elif user_selection == 'all':
            new_list = date_results
    return new_list