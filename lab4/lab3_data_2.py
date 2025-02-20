from datetime import date,timedelta
yesterday=date.today()-timedelta(days=1)
today=date.today()
tomorrow=date.today()+timedelta(days=1)
print("yesterday:",yesterday)
print("today:",today)
print("tomorrow:",tomorrow)