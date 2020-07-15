from fbchat import Client
from fbchat.models import *


client = Client('python.analyssis@gmail.com', 'Pythonisbest')

client.send(Message(text='hello', thread_id='100014168110507', thread_type=ThreadType.USER))






