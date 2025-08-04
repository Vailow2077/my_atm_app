import time
##
### Получение текущего времени в формате timestamp
##timestamp = time.time()
##
##print("Текущий timestamp:", timestamp)
##
from datetime import datetime
##
##real_time = datetime.now().strftime("%Y-%m-%d %H:%M")
##print("Текущее время:", real_time)



# Ввод и преобразование дат

while True:
    start_date_str = input("Введите начальную дату (в формате ГГГГ-ММ-ДД): ")
    try:
        start_ts = int(datetime.strptime(start_date_str, "%Y-%m-%d").timestamp())
        break
    except ValueError:
        print("Неправильный формат даты. Используй ГГГГ-ММ-ДД.")

while True:
    end_date = input()
    try:
        end_ts = int(datetime.strptime(end_date, "%Y-%m-%d").replace(hour=23, minute=59, second=59).timestamp())
        break
    except ValueError:
        print()


