#імпорт бібліотеки random та курсору бази даних
from database import mycursor
from database import mydb

#Функція, що додає запис до бази даних
def addProp(message):
    mycursor.execute("""
    insert into feedback(msg)
    values
    ("{var}");""".format(var=message))
    mydb.commit()
