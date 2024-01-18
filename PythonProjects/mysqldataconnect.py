import datetime
import mysql.connector

# mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("SHOW TABLES")
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), adress VARCHAR(255))")

"""
def InsertProduct(name,price,imageUrl,descripton):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="node-app"
    )
    cursor = connection.cursor()

    sql = "INSERT INTO products(name, price, imageUrl, description) VALUES (%s, %s, %s, %s)"
    values = (name,price,imageUrl,descripton)

    cursor.execute(sql,values)

    try:
        connection.commit()
    except mysql.connector.Error as err:
        print("Error: ", err)
    finally:
        connection.close()
        print("Bitti")

def InsertProducts(liste):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="node-app"
    )
    cursor = connection.cursor()

    sql = "INSERT INTO products(name, price, imageUrl, description) VALUES (%s, %s, %s, %s)"
    values = liste

    cursor.executemany(sql,values)

    try:
        connection.commit()
    except mysql.connector.Error as err:
        print("Error: ", err)
    finally:
        connection.close()
        print("Bitti")


liste = []

while True:
    name = input("Name: ")
    price = input("Price: ")
    imageUrl = input("ImageUrl: ")
    description = input("Description: ")

    liste.append((name,price,imageUrl,description))

    result = input("Devam etmek? e/h : ")
    if result == "h":
        print("Database'e aktarılıyor")
        print(liste)
        InsertProducts(liste)
        break
"""

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "schooldb"
)

cursor = connection.cursor()

sql = "INSERT INTO students(StudentNumber, name, surname, Birthday, Gender) VALUES (%s, %s, %s, %s, %s)"
ogrenciler = [
    ("104","Veli","Kara",datetime.datetime(2006,2,19),"E"),
    ("105","Duran","Ali",datetime.datetime(2006,6,11),"E"),
    ("106","Mehmet","Kar",datetime.datetime(2006,7,25),"K")
]

cursor.executemany(sql,ogrenciler)

try:
    connection.commit()
    print(f"{cursor.rowcount} tane kayıt eklendi")
except mysql.connector.Error as err:
    print("Hata: ", err)
finally:
    connection.close()