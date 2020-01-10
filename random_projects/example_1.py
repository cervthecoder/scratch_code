from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.novinky.cz/zahranicni').text

soup = BeautifulSoup(source, 'lxml')

#print(soup.prettify())

news = [article.text for article in soup.find_all('div', class_='f_bL')]
print(news)


#https://www.novinky.cz/domaci


