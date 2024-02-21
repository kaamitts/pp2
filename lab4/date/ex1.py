#Write a Python program to subtract five days from current date.

from datetime import datetime, timedelta

current_date = datetime.now()

new_data = (current_date - timedelta(days=5)).date()

print(new_data)