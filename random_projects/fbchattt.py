from fbchat import Client
import requests
from fbchat.models import *

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = "Prague"
url = api_address + city
json_data = requests.get(url).json()
format_add = json_data["main"]

temperature = json_data['main']['temp']
pressure = json_data['main']['pressure']
humidity = json_data['main']['humidity']

message = "Temperature: " + str(temperature) + " K\n Pressure: " + str(pressure) + " mbar\nHumidity: " + str(
    humidity) + "%"


client = Client('python.analyssis@gmail.com', 'Pythonisbest')
client.send(Message(text=message), thread_id=100014168110507, thread_type=ThreadType.USER)
client.logout()
