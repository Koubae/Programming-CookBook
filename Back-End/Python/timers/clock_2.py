from datetime import datetime, timedelta

def add_time(start, duration, start_weekday=None):

    weekdays = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
        'Saturday', 'Sunday'
        ]
    # Process the time, convert from String ---> To a Datetime Object in the 12 h 
    proc_t = datetime.strptime(start, '%I:%M %p')
    dur = duration.split(':')
    
    # Calculates excactly the time passed, assigning PM/AM
    new_time = proc_t + timedelta(hours=int(dur[0]), minutes=int(dur[1]))

    # Get Days passed
    days = int(dur[0]) // 24
    # Adding a new day if time passes Midnight
    if proc_t.strftime('%p') == 'PM' and new_time.strftime('%p')== 'AM':
        days +=1

    # Formatting the Time From DateTIme Object ----> String
    new_time = new_time.strftime('%I:%M %p')
    
    

    # Get the new weekday
    if start_weekday:
        start_day_idx = weekdays.index(start_weekday.title())
        new_weekday = weekdays[(start_day_idx + days % 7)  % 7]
   
    new_time = f'New Time is >> {new_time}'
    if start_weekday: 
        new_time += f'- {new_weekday} -'
    if days == 1:
        new_time += ' (new day)'
    elif days > 1:
        new_time += f' -Total days: {days}- <<'
   
    
    return new_time

print('---'*30)
x = add_time('11:00 PM', '0:30', 'Monday')
print(x)
print('---'*30)



