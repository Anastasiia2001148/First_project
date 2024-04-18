
from datetime import datetime
def get_days_from_today(date):
   try:
        date_old = datetime.strptime(date, '%Y-%m-%d').date()
        current_date = datetime.today().date()
        if date_old > current_date:
            count_days = date_old-current_date
            return print(count_days.days)
        elif date_old < current_date:
            count_days = current_date - date_old
            return print(-count_days.days)
        else:
            return print('Dates are equal')
   except ValueError:
    return print("Does not match format")

get_days_from_today('2024-06-09')

