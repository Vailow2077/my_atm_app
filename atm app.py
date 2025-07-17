import random
import sqlite3

connection = sqlite3.connect('my_database.db')  # Устанавливаем соединение с базой данных
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Bank (
id integer,
log TEXT,
password TEXT,
balance integer
)''')   # Создаем таблицу Bank

print ("welcome to my bank! do you new user or old?")
print ("1 - new:")
print ("2 - old:")

list_1 = ["1", "2"]
while True:
    a = input()
    if a in list_1:
        break
    else:
        print ("invalid input:")
a = int(a)

if a == 1:
    while True:
        id = random.randint(100000, 999999)
        cursor.execute('SELECT * FROM Bank WHERE id = ?', (id,)) # ищем id
        result = cursor.fetchone()
        if result == None:
            break  # ID уникален, выходим из цикла
    print  ("creative your log-in:")
    log = (input())
    print ("your log-in is:", log)
    print ("creative your password:")
    password = (input())
    print ("your password is:", password)
    print ("write your password:")
    b = (input())
    x = 1
    while b != password:
        print ("write correct password:")
        b = (input())
        x += 1

        if x == 5:
            print ("you write incorrect password. try again!")
            raise SystemExit
    if b == password:
        print("done:")

    cursor.execute('INSERT INTO Bank (id, password, log) VALUES (?, ?, ?)',(id ,password, log))  # Добавляем нового пользователя
    connection.commit()  # Сохраняем изменения

    balance = random.randint(1, 100000)
    print ("login completed, your balance is:", balance)

    cursor.execute('UPDATE Bank SET balance = ? WHERE ID = ?', (balance, id))  # Добавляем данные
    connection.commit() # Сохраняем изменения

if a == 2:
    print ("write your log-in:")
    log = input()
    print ("write your password:")
    password = input()

    cursor.execute('SELECT balance FROM Bank WHERE log = ? AND password = ?', (log, password)) #ищем переменную баланс в таблице и даем ее результу
    result = cursor.fetchone() # результ

    if result is not None: # если результ найден то будет что то если нет то ошибка
        balance = result[0]
        print ("login completed, your balance is:", balance)
    else:
        print ("login don't done, id or password incorrect:")
        connection.close()
        raise SystemExit

while True:
    print ("what you want do?")
    print ("1 - to replenish:")
    print ("2 - to remove:")
    print ("3 - nothing:")

    list_2 = ["1", "2", "3"]
    while True:
        d = input()
        if d in list_2:
            break
        else:
            print("invalid input:")
    d = int(d)

    if d == 1:
        print ("how money you want to replenish?")
        while True:
            try:
                i = int(input())
                while i <= 0:
                    print('incorrect:')
                    i = int(input())
                break
            except ValueError:
                print("incorrect input:")
        print ("write your password:")
        b = (input())
        while b != password:
            print('write correct password:')
            b = (input())
        if b == password:
            print ("done:")
        balance = i + balance

        cursor.execute('UPDATE Bank SET balance = ? WHERE ID = ?', (balance, id))  # Добавляем данные
        connection.commit()  # Сохраняем изменения

        print ("done:")
        print ("your balance is:", balance)

    if d == 2:
        print ("how money you want to remove?")
        while True:
            try:
                f = int(input())
                while f > balance:
                    print('incorrect:')
                    f = int(input())
                while f <= 0:
                    print('incorrect input:')
                    f = int(input())
                break
            except ValueError:
                print("incorrect input:")
        print ("write your password:")
        b = (input())
        while b != password:
            print('write correct password:')
            b = (input())
        if b == password:
            print("done:")
        balance = balance - f

        cursor.execute('UPDATE Bank SET balance = ? WHERE ID = ?', (balance, id))  # Добавляем данные
        connection.commit()  # Сохраняем изменения

        print ("done:")
        print("your balance is:", balance)

    if d == 3:
        print ("ok, thank you for use our bank! come back!")
        connection.close()

        break