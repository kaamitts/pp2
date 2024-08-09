import psycopg2

connection = None

try:
    connection = psycopg2.connect(
        host = "127.0.0.1",
        user = "postgres",
        password = "qwerty" + "123",
        database = "bot_users"
    ) 
    
    connection.autocommit = True 
    
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version()"
        )
        print(f"Server version: {cursor.fetchone()}" )
        
    #create a new table
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users(
                id serial PRIMARY KEY,
                first_name VARCHAR(50) NOT NULL,
                nick_name VARCHAR(50) NOT NULL);"""
        )
        print("[INFO] table created successfely")
        
    #insert data into a table
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO users (firat_name, nick_name) VALUES
            ('Oleg', 'barracuda');"""
        )
        print("[INFO] Data was successfuly inserted")
    
    #get data from a table
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT nick_name FROM users WHERE first_name = 'Oleg';"""
        )

        print(cursor.fetchone())
        
    #dalete table
    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE users;"""
        ) 
        
        print("[INFO] Table was deleted")
        
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")