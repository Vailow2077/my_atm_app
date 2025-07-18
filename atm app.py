import random
import sqlite3
import hashlib

connection = sqlite3.connect('bank_database.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Bank (
user_id integer,
log TEXT,
password TEXT,
history TEXT,
balance integer
)''')

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
        user_id = random.randint(100000, 999999)
        cursor.execute('SELECT * FROM Bank WHERE user_id = ?', (user_id, ))
        result = cursor.fetchone()
        if result == None:
            break
    print  ("creative your log-in:")
    log = (input())
    print ("your log-in is:", log)
    print ("creative your password:")
    password = (input())
    print ("your password is:", password)
    encoded = password.encode('utf-8')
    saved_hash = hashlib.sha256(encoded).hexdigest()
    print ("write your password:")
    b = (input())
    input_hash = hashlib.sha256(b.encode()).hexdigest()
    x = 1
    while input_hash != saved_hash:
        print ("write correct password:")
        b = (input())
        x += 1

        if x == 5:
            print ("you write incorrect password. try again!")
            raise SystemExit
    if input_hash == saved_hash:
        print("done:")

    cursor.execute('INSERT INTO Bank (user_id, password, log) VALUES (?, ?, ?)',(user_id ,saved_hash, log))
    connection.commit()

    balance = random.randint(1, 100000)
    history = ""
    print ("login completed, your balance is:", balance)

    cursor.execute('UPDATE Bank SET balance = ?, history = ? WHERE user_id = ?', (balance, history , user_id))
    connection.commit()

if a == 2:
    print ("write your log-in:")
    log = input()

    cursor.execute('SELECT password FROM Bank WHERE log = ?', (log, ))
    result = cursor.fetchone()

    if result is not None:
        saved_hash = result[0]
        print("log-in correct, write your password:")
    else:
        print("log-in incorrect:")
        connection.close()
        raise SystemExit
    print ("write your password:")
    b = input()
    input_hash = hashlib.sha256(b.encode()).hexdigest()

    cursor.execute('SELECT balance, history, user_id FROM Bank WHERE log = ? AND password = ?', (log, saved_hash)) #ищем переменную баланс в таблице и даем ее результу
    result = cursor.fetchone() # результ

    if result is not None: # если результ найден то будет что то если нет то ошибка
        balance = result[0]
        history = result[1]
        user_id = result[2]
        print ("login completed, your balance is:", balance)
    else:
        print ("login don't done, log-in or password incorrect:")
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
        input_hash = hashlib.sha256(b.encode()).hexdigest()
        while input_hash != saved_hash:
            print('write correct password:')
            b = (input())
        if input_hash == saved_hash:
            print ("done:")
        balance = i + balance
        history = " +" + str(i)

        cursor.execute('UPDATE Bank SET balance = ? WHERE user_id = ?', (balance, user_id)) # Добавляем данные
        cursor.execute('UPDATE Bank SET history = history || ? WHERE user_id = ?', (history, user_id))
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
        input_hash = hashlib.sha256(b.encode()).hexdigest()
        while input_hash != saved_hash:
            print('write correct password:')
            b = (input())
        if input_hash == saved_hash:
            print("done:")
        balance = balance - f
        history = " -" + str(f)

        cursor.execute('UPDATE Bank SET balance = ? WHERE user_id = ?', (balance, user_id))  # Добавляем данные
        cursor.execute('UPDATE Bank SET history = history || ? WHERE user_id = ?', (history, user_id))
        connection.commit()  # Сохраняем изменения

        print ("done:")
        print("your balance is:", balance)

    if d == 3:
        print ("ok, thank you for use our bank! come back!")
        connection.close()

        break