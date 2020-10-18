


def add_time(start, duration, start_weekday=None):

    weekdays = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
        'Saturday', 'Sunday'
        ]
    start_time, period = start.split(' ')
   
    def process_time():
   
        time_array = ([int(t) for t in start_time.split(":")]),([int(d) for d in duration.split(":")])
        end_hours, end_mins = (time_array[0][0] + time_array[1][0], time_array[0][1] + time_array[1][1])
        days = int(end_hours/24)

        new_time_array = [ str(end_hours % 12 + end_mins // 60), ':', (str(end_mins % 60).rjust(2, '0'))]
        new_time_joined = ''.join(new_time_array)
        end_period = [period]
        clock = end_hours // 12

        if start_weekday:
            start_day_idx = weekdays.index(start_weekday.title())
            new_weekday = weekdays[(start_day_idx + days % 7)  % 7]
        else:
            new_weekday = False
        
        for i in range(clock):
            if end_period[-1].lower() == 'am':
                end_period.append('PM')
            else:
                end_period.append('AM')

        return new_time_joined, end_period, new_weekday, days  

    t_output = process_time()
    def process_output():

        new_time = f'New Time is >> {t_output[0]} {t_output[1][-1]}'
        if t_output[2]: 
            new_time += f'- {t_output[2]} -'
        if t_output[3] == 1 and (period != t_output[1] or t_output[1] == 'AM'):
            new_time += ' (new day)'
        elif t_output[3] > 1:
            new_time += f' -Total days: {t_output[3]}- <<'
        return new_time
    print(t_output[3])
    new_time = process_output()

    return new_time

print('---'*30)
x = add_time('10:00 AM', '54:00', 'Monday')
print(x)
print('---'*30)