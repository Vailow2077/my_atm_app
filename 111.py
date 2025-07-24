import time
from datetime import datetime

# Получаем текущий timestamp (в секундах)
a = int(time.time())
print("a (timestamp в секундах):", a)

# Преобразуем a в читаемую дату и время
b = datetime.fromtimestamp(a)
print("b (дата и время):", b.strftime("%Y-%m-%d %H:%M:%S"))
