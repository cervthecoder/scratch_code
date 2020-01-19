# import Adafruit_DHT
import matplotlib as plt
import time
from fbchat import Client
from fbchat.models import *


def get_temp(pin):
    hum, temp = Adafruit_DHT.read_retry(sensor, pin)
    return [hum, temp]

def send_message(message):
    client = Client('python.analyssis@gmail.com', 'Pythonisbest')
    client.send(Message(message), thread_type=ThreadType.USER, thread_id='users id')
    client.logout()

if '__main__' == __name__:
    # while True:
    #     if time.localtime().tm_min = 0:
    #         pass
    print(time.localtime().tm_min)
            





