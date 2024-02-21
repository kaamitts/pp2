#Write a Python program to calculate two date difference in seconds.
from datetime import datetime

date1 = datetime(2024, 1, 1, 12, 0, 0)
date2 = datetime(2024, 1, 1, 14, 30, 0)
difference = date2 - date1
diff_sec = difference.total_seconds()
print(diff_sec)