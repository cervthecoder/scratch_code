from bs4 import BeautifulSoup

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


list_ar = [article.p.text for article in soup.find_all('div', class_='article')]
print(list_ar)

match = soup.find_all('div', class_='article')




nwm = soup.title.text
print(nwm)

