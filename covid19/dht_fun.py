import Adafruit_DHT
import time
from fbchat import Client
from fbchat.models import *


def get_temp(pin):
    hum, temp = Adafruit_DHT.read_retry(11, pin)
    return [hum, temp]

def send_message(message):
    client = Client('example@mail.com', 'Password')
    client.send(Message(text=message), thread_type=ThreadType.USER, thread_id='users id')
    client.logout()

if '__main__' == __name__:
    while True:
        if time.localtime().tm_min == 0 and time.localtime().tm_sec==0:
            hum, temp = get_temp(17)
            send_message('Hello')
            send_message(f'Vlhkost v pokoji - {hum} % \nTeplota v pokoji {temp}')

            
