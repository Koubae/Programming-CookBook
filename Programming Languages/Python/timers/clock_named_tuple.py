from collections import namedtuple


MainTimer = namedtuple('MainTimer', 'new_time_joined, end_period, new_weekday, days')


def add_time(start, duration, start_weekday=None):

    weekdays = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
        'Saturday', 'Sunday'
        ]
    start_time, period = start.split(' ')

    def process_time():

        current_hour, current_minute = ([int(t) for t in start_time.split(':')])
        end_hour, end_minute = ([int(d) for d in duration.split(':')])

        # Adds Current time plus End Time Total
        end_hours, end_mins = (current_hour + end_hour, current_minute + end_minute)
        # Calculates Total days passed
        days = int(end_hours/24)
        # Calculates New Time
        new_time_array = [str(end_hours % 12 + end_mins // 60), ':', str(end_mins % 60).rjust(2, '0')]
        new_time_joined = ''.join(new_time_array)

        end_period = [period]
        # Clock, calculates the days elapsed
        clock = end_hours // 12

        if start_weekday:
            start_day_idx = weekdays.index(start_weekday.title())
            new_weekday = weekdays[(start_day_idx + days % 7) % 7]
        else:
            new_weekday = False
        # Figure out whether is AM or PM
        for i in range(clock):
            if end_period[-1].lower() == 'am':
                end_period.append('PM')
            else:
                end_period.append('AM')
        return MainTimer(new_time_joined, end_period, new_weekday, days)

    # Triggers process time function
    timed = process_time()

    def process_output():

        new_time = f'New Time is >>> {timed.new_time_joined} {timed.end_period[-1]}'
        if timed.new_weekday:
            new_time += f'- {timed.new_weekday} -'
        if timed.days == 1 and (period != timed.end_period or timed.end_period == 'AM'):
            new_time += ' (new_day)'
        elif timed.days > 1:
            new_time += f' -Total days: {timed.days}- <<'
        return new_time

    new_time = process_output()

    return new_time


print('---'*30)
x = add_time('10:00 AM', '54:00', 'Monday')
print(x)
print('---'*30)