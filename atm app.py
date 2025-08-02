import random
import sqlite3          #импотрируем таблицу
import hashlib          #импортируем кодирование пароля
import time                     #для время
from datetime import datetime   #для время

connection = sqlite3.connect('bank_database.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Connect (
user_id INTEGER PRIMARY KEY AUTOINCREMENT,
log_in TEXT,
password TEXT
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Information (
user_id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT,
last_name TEXT
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Operations (
user_id integer,
balance integer,
history TEXT,
timestamp integer
)''')

print ("welcome to my bank! do you new user or old?")
print ("1 - new:")
print ("2 - old:")
list_1 = ["1", "2"]
while True:
    choice_1 = input()
    if choice_1 in list_1:
        break
    else:
        print ("invalid input:")
choice_1 = int(choice_1)

if choice_1 == 1:
    while True:
        print ("write your first name:")
        first_name_1 = input().strip()              #стрип удаляет все пробелы
        if first_name_1.isalpha():                  #исалпха проверяет состоит ли текст только из букв
            first_name = first_name_1.capitalize()  #капитализ делает имя как имя с заглывной буквы
        else:
            print("invalid input:")
        print ("your first name is:", first_name, "?")
        print ("1 - yes:")
        print ("2 - no:")
        choice_2 = input()
        list_1 = ["1", "2"]
        while True:
            if choice_2 in list_1:
                break
            else:
                print("invalid input:")
                choice_2 = input()
        choice_2 = int(choice_2)
        if choice_2 == 1:
            break

    while True:
        print ("write your last name:")
        last_name_1 = input().strip()               #стрип удаляет все пробелы
        if last_name_1.isalpha():                   #исалпха проверяет состоит ли текст только из букв
            last_name = last_name_1.capitalize()    #капитализ делает имя как имя с заглывной буквы
        else:
            print("invalid input:")
        print ("your last name is:", last_name, "?")
        print ("1 - yes:")
        print ("2 - no:")
        choice_3 = input()
        list_1 = ["1", "2"]
        while True:
            if choice_3 in list_1:
                break
            else:
                print("invalid input:")
                choice_3 = input()
        choice_3 = int(choice_3)
        if choice_3 == 1:
            break

    def add_user(log_in):
        cursor.execute("INSERT INTO Connect (log_in) VALUES (?)", (log_in,))
        connection.commit()
        return cursor.lastrowid       #создаем лог ин и возвращаем последние id для правильной маркировки

    print  ("creative your log-in:")
    log_in = (input())
    print ("your log-in is:", log_in)
    user_id = add_user(log_in)        #задаем айди

    print ("creative your password:")
    password = (input())
    print ("your password is:", password)
    encoded = password.encode('utf-8')                      #задаем строку в байты для кодирования
    saved_hash = hashlib.sha256(encoded).hexdigest()        #вычесляем с помощью библиотеки hashlib sha 256 хеш битов(способ кодирования) и hexdigest возвращает 16-ричный код
    print ("write your password:")
    choice_4 = (input())
    input_hash = hashlib.sha256(choice_4.encode()).hexdigest()
    x = 1
    while input_hash != saved_hash:
        print ("write correct password:")
        choice_4 = (input())
        x += 1
        if x == 5:
            print ("you write incorrect password. try again!")
            raise SystemExit
    if input_hash == saved_hash:
        print("done:")

    balance = random.randint(1, 100000)
    history = ""
    timestamp = 0                   #время в секундах с 01.01.1970
    print ("login completed, your balance is:", balance)

    cursor.execute('UPDATE Connect SET password = ?, log_in = ? WHERE user_id = ?',(saved_hash, log_in, user_id))
    connection.commit()
    cursor.execute("INSERT INTO Information (user_id, first_name, last_name) VALUES (?, ?, ?)", (user_id, first_name, last_name))
    connection.commit()
    cursor.execute("INSERT INTO Operations (user_id, history, balance, timestamp) VALUES (?, ?, ?, ?)", (user_id, history, balance, timestamp))
    connection.commit()

if choice_1 == 2:
    print ("write your log-in:")
    log_in = input()

    cursor.execute('SELECT password FROM Connect WHERE log_in = ?', (log_in, ))
    result = cursor.fetchone()        #достаем одну строчку и даем ее результу, если результ не ноль то там значение если ноль то ничего не нашел
    if result is not None:
        saved_hash = result[0]
        print("log-in correct, write your password:")
    else:
        print("log-in incorrect:")
        connection.close()
        raise SystemExit
    print ("write your password:")
    choice_5 = input()
    input_hash = hashlib.sha256(choice_5.encode()).hexdigest()     #опять шифруем пароль

    cursor.execute('SELECT user_id FROM Connect WHERE log_in = ? AND password = ?', (log_in, saved_hash,)) #ищем переменную в таблице и даем ее результу
    result = cursor.fetchone() # результ
    if result is not None: # если результ найден то будет что то если нет то ошибка
        user_id = result[0]
    else:
        print("login don't done, log-in or password incorrect:")
        connection.close()
        raise SystemExit

    cursor.execute('SELECT first_name, last_name FROM Information WHERE user_id = ?', (user_id, ))  # ищем переменную в таблице и даем ее результу
    result = cursor.fetchone()  # результ
    if result is not None:  # если результ найден то будет что то если нет то ошибка
        first_name = result[0]
        last_name = result[1]
    else:
        print("login don't done, log-in or password incorrect:")
        connection.close()
        raise SystemExit

    cursor.execute('SELECT balance, timestamp, history  FROM Operations WHERE user_id = ?', (user_id,))  # ищем переменную в таблице и даем ее результу
    result = cursor.fetchone()  # результ
    if result is not None:  # если результ найден то будет что то если нет то ошибка
        balance = result[0]
        timestamp = result[1]
        history = result[2]
    else:
        print("login don't done, log-in or password incorrect:")
        connection.close()
        raise SystemExit

    print("login completed, your balance is:", balance)

while True:
    print ("what you want do?")
    print ("1 - to replenish:")
    print ("2 - to remove:")
    print ("3 - nothing:")
    list_2 = ["1", "2", "3"]
    while True:
        choice_6 = input()
        if choice_6 in list_2:
            break
        else:
            print("invalid input:")
    choice_6 = int(choice_6)

    if choice_6 == 1:
        print ("how money you want to replenish?")
        while True:
            try:
                choice_7 = int(input())
                while choice_7 <= 0:
                    print('incorrect:')
                    choice_7 = int(input())
                break
            except ValueError:
                print("incorrect input:")

        print ("write your password:")
        choice_8 = (input())
        input_hash = hashlib.sha256(choice_8.encode()).hexdigest()
        while input_hash != saved_hash:
            print('write correct password:')
            choice_8 = (input())
        if input_hash == saved_hash:
            print ("done:")

        balance = choice_7 + balance
        history = " +" + str(choice_7)
        sec = int(time.time())                    # Получаем текущий timestamp (в секундах)
        real_time = datetime.fromtimestamp(sec)           # Преобразуем в читаемую дату и время
        #print(real_time.strftime("%Y-%m-%d %H:%M:%S"))   #вывод времени
        cursor.execute("INSERT INTO Operations (user_id, balance, history, timestamp) VALUES (?, ?, ?, ?)",(user_id, balance, history, sec))
        connection.commit()
        print ("done:")
        print ("your balance is:", balance)

    if choice_6 == 2:
        print ("how money you want to remove?")
        while True:
            try:
                choice_9 = int(input())
                while choice_9 > balance:
                    print('incorrect:')
                    choice_9 = int(input())
                while choice_9 <= 0:
                    print('incorrect input:')
                    choice_9 = int(input())
                break
            except ValueError:
                print("incorrect input:")

        print ("write your password:")
        choice_8 = (input())
        input_hash = hashlib.sha256(choice_8.encode()).hexdigest()
        while input_hash != saved_hash:
            print('write correct password:')
            choice_8 = (input())
        if input_hash == saved_hash:
            print("done:")

        balance = balance - choice_9
        history = " -" + str(choice_9)
        sec = int(time.time())                   # Получаем текущий timestamp (в секундах)
        real_time = datetime.fromtimestamp(sec)  # Преобразуем в читаемую дату и время
        cursor.execute("INSERT INTO Operations (user_id, balance, history, timestamp) VALUES (?, ?, ?, ?)",(user_id, balance, history, sec))
        connection.commit()
        print ("done:")
        print("your balance is:", balance)

    if choice_6 == 3:
        print ("ok, thank you for use our bank! come back!")
        connection.close()
        break