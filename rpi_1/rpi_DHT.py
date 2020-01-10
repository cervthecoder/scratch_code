import adafruit_dht as dht
from board import 17

dht_11 = dht.DHT11(17)

def get_temperature():
    return dht_device.temperature

def get_humidity():
    return dht_device.humidity

if __main__ = '__name__':
    temp = get_temperature()
    hum = get_humidity()
    print(f"{temp} °C \n {hum} %")
