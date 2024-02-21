#Write a Python program to drop microseconds from datetime.
from datetime import datetime, timedelta

current_data = datetime.now()
without_mcrs = current_data.replace(microsecond=0)
print(without_mcrs)