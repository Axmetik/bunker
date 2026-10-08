#імпорт конектора для бази даних
import os
import mysql.connector

#Під'єднання бази даних
mydb = mysql.connector.connect(
    host=os.getenv('DB_HOST', 'localhost'),
    password=os.getenv('DB_PASSWORD', ''),
    user=os.getenv('DB_USER', 'root'),
    database=os.getenv('DB_NAME', 'bunker')
)

#Створення курсору для виконання дій над базою даних
mycursor = mydb.cursor()
