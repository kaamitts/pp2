#Write a Python program to print yesterday, today, tomorrow.

from datetime import datetime, timedelta

yesterday = (datetime.now()-timedelta(days=1)).date()
today = (datetime.now()).date()
tomorrow = (datetime.now()+timedelta(days=1)).date()
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)