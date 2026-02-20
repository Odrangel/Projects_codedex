import datetime, bday_messages as bm

today = datetime.datetime.today()
next_birthday = datetime.datetime(2026,11,5)

time_difference = next_birthday - today
print(today)
if time_difference == next_birthday:
    print(bm.random_message)
else:
    print(f'Mi cumpleaños esta a {time_difference} dias ')



