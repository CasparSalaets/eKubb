import maakserver
import time

while True:
    data = maakserver.pollserver()
    if data is not None:
        print(data)
        maakserver.sendserver(str(data) + ' was sent by the pico')
    time.sleep(0.1)
