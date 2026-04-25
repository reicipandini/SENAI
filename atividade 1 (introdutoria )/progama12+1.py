import time

tempo = 10
while tempo > 0:
    print("Tempo restante:", tempo, "segundos")
    time.sleep(1)
    tempo -= 1
print("Prensa liberada!")