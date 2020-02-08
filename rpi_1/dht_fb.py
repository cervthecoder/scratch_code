import Adafruit_DHT
import matplotlib as plt
import time
from fbchat import Client
from fbchat.models import *


def get_temp(pin):
    hum, temp = Adafruit_DHT.read_retry(sensor, pin)
    return [hum, temp]

def send_message(message):
    client = Client('example@mail.com', 'Password')
    client.send(Message(message), thread_type=ThreadType.USER, thread_id='users id')
    client.logout()

if '__main__' == __name__:
    while True:
        hum_list = []
        temp_list = []
        hour_list = []
        if time.localtime().tm_min == 0:
            hum_list.append(get_temp(4)[0])
            temp_list.append(get_temp(4)[1])
            hour_list.append(time.localtime().tm_hour)

        if time.localtime().tm_hour == 17 and time.localtime().tm_min == 0:
            send_message(plt.plot(temp_list, hour_list))
            send_message(plt.plot(hum_list, hour_list))
            hum_list.clear()
            temp_list.clear()
            hour_list.clear()
