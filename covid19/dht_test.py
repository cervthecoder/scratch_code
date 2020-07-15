import Adafruit_DHT
from fbchat import Client
from fbchat.models import *
import time

def get_temp(pin):
    hum, temp = Adafruit_DHT.read_retry(11, pin)
    return [hum, temp]

print(get_temp(17))
print(time.localtime().tm_hour)
client = Client('p@gmail.com', 'Pytest')
info = get_temp(17)
message = str(info[0])+str(info[1])
print(message)
client.send(Message(text=message), thread_type=ThreadType.USER, thread_id='100014168110507')
client.logout()


