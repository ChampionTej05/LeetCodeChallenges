import sqlite3

#connect to local db 
try:
    with sqlite3.connect("mydb.db") as connection:

        cursor = connection.cursor()

        sql_query = """
        CREATE TABLE IF NOT EXISTS users(
        id INTERGER PRIMARY KEY, 
        name TEXT NOT NULL,
        age INTEGET NOT NULL
        );
        """
        cursor.execute(sql_query)


        insert_query = """
        INSERT INTO users (
        id, name, age
        ) VALUES (
            ?, ?, ?
            );
        """

        cursor.execute(insert_query, (2, "Rakshit", 12))


        users = [
            (2, 'Bob', 25),
            (3, 'Charlie', 35),
            (4, 'David', 40)
        ]
        cursor.executemany(insert_query, users)

        select_query = """
        SELECT * FROM users where age > ?;
        """
        #qmark style
        params = (10,)
        cursor.execute(select_query, params)
        # result = cursor.fetchall()
        # for row in result:
        #     print(row)

        #gives next row only
        row = cursor.fetchone()
        while row : 
            print(row)
            row = cursor.fetchone()


        connection.commit()
except sqlite3.IntegrityError as e:
    print("Exception, ", e)
    connection.rollback()
except Exception as e:
    print(e)
    connection.rollback()



# Teardown for the DB 

import os
os.remove('mydb.db')