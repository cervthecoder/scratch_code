import requests
from bs4 import BeautifulSoup
from fbchat import Client
from fbchat.models import *
import time


client = Client('python.analyssis@gmail.com', 'Pythonisbest')


def get_count():
    url = 'https://onemocneni-aktualne.mzcr.cz/covid-19'
    con = requests.get(url).text
    soup = BeautifulSoup(con)
    count = [article.text for article in soup.find_all('p')]
    return [count[7], count[9], count[11]]

while True:
    if time.localtime().tm_hour==13 and time.localtime().tm_min==4 and time.localtime().tm_sec==0:
        client.send(Message(text=f'celkem nakazenych - {get_count()[0]}\nCelkovy pocet vylecenych  - {get_count()[1]}\nCelkovy pocet umrti - {get_count()[2]}'), thread_id='2674445732584644', thread_type=ThreadType.GROUP)




