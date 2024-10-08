# maakserver.py

import socketpool
import wifi
import json
from adafruit_httpserver import Server, Request, Response, GET, Websocket

SSID = "ESAT6B1"
PASSWORD = "ESATK19"
wifi.radio.start_ap(ssid=SSID, password=PASSWORD)
print("My IP address is", wifi.radio.ipv4_address_ap)
pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static", debug=True)
websocket = None

@server.route("/connect-websocket", GET)
def connect_client(request: Request):
    global websocket
    if websocket is not None:
        websocket.close()
    websocket = Websocket(request)
    return websocket

server.start(str(wifi.radio.ipv4_address_ap))

def pollserver():
    server.poll()
    if websocket is not None:
        data = websocket.receive(fail_silently=True)
        if data is not None:
            try:
                return json.loads(data)
            except:
                return data

def sendserver(message):
    if websocket is not None:
        websocket.send_message(json.dumps(message), fail_silently=True)
        