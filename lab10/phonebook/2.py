import psycopg2
import csv

def update(sn, mode, newv):
    cursor.execute("""UPDATE PhoneBook SET {} = '{}' WHERE surname = '{}' """.format(mode, newv, sn))
    connection.commit()

def delete(sn):
    cursor.execute("""DELETE FROM PhoneBook WHERE surname = '{}' """.format(sn))
    connection.commit()

connection = None

try: 
    connection = psycopg2.connect(
        host = "localhost",
        database = "lab10",
        user = "admin",
        password = "qwerty"        
    )
    connection.autocommit()
    
    #Create a table
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXIST Phonebook 
        (id serial PRIMARY KEY, surname VARCHAR(255), name VARCHAR(255), number INT)""")
        print("[INFO] Table created successfely")
        
#Inserting data in table
    #inserting from console
    with connection.cursor() as cursor:
        mode = "enter"
        while True:
            print("[INFO] Print 'enter' if you want to insert new data and type 'stop' to break")
            if mode  == "stop":
                break
            balada = []
            print("Enter a surname:")
            balada.append(input())
            print("Enter a name:")
            balada.append(input())
            print("Enter a number")
            balada.append(input())
            balada = tuple(balada)
            cursor.execute("""INSERT INTO PhoneBook (surname, name, number) VALUES {};""".format(balada))
    #Insertin from csv file
    with connection.cursor() as cursor:
        while True:
            print("[INFO] Print 'yes' if you want to insert new data from csv file and type 'no' to break")
            mode = input()
            if mode == "no":
                break
            print("enter the name of the file")
            mode = input()
            with open(mode + ".csv", "r") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cursor.execute("""INSERT INTO PhoneBook VALUES (%s, %s, %s)""", row)     
    #Updating data
    with connection.cursor() as cursor:
        while True:
            print("Type 'update' to update some data or 'stop' to break")
            mode = input()
            if mode == "stop":
                break
            cursor.execute("""SELECT * FROM PhoneBook""")
            print(cursor.fetchall())
            print("Enter surname")
            sn= input()
            print("What you want to change? name/number")
            mode = input()
            print("Enter new name/number")
            newvalue = input()
            update(sn, mode, newvalue)                    
                    
    with connection.cursor() as cursor:
        # DELETING DATA-----------
        while True:
            print("want to delete some data? yes/no")
            mode = input()
            if mode == "no":
                break
            cursor.execute("""SELECT * FROM PhoneBook""")
            print(cursor.fetchall())
            print("Enter surname")
            idtodelete = input()
            delete(idtodelete)           
                        
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")