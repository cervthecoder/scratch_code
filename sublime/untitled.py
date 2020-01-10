import requests

url = 'https://newsapi.org/v2/everything?domains=wsj.com&apiKey=3a420d3c1ad04181bdd80b8d60584a44'

content = requests.get(url).json()


inside = content['articles']

articles = [con['title'] + " - " + con['content'] for con in inside]

i = 0 
for article in articles:
	i += 1
	print(article + "\n")
	if i == 5:
		break




