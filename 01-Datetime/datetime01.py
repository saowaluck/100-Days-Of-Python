from datetime import datetime, date, timedelta

today = datetime.today()
today_date = date.today()

nextyear = timedelta(days=365) + today
new_year = date(nextyear.year, 1, 1)
countdown = (new_year - today_date).days

print('#' * 20 + ' HAPPY NEW YEAR ' + '#' * 20)
print(f'countdown: {countdown} days')
print('#' * 56)
