import time

# Получение текущего времени в формате timestamp
timestamp = time.time()

print("Текущий timestamp:", timestamp)

from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Текущее время:", current_time)
