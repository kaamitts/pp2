from datetime import timedelta, datetime
str_date1 = input("Введите первую любую дату в виде ГГГГ-ММ-ДД: ")
date1 = datetime.strptime(str_date1, "%Y-%m-%d")
str_date2 = input("Введите втроую любую дату в виде ГГГГ-ММ-ДД: ")
date2 = datetime.strptime(str_date2, "%Y-%m-%d")
new_date = abs((date1 - date2).total_seconds())
print(new_date)