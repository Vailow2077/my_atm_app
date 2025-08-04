while True:
        user_id = random.randint(100000, 999999)
        cursor.execute("SELECT 1 FROM Users WHERE user_id = ?", (user_id,))
        if not cursor.fetchone():
            return user_id  # этот ID ещё не используется





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