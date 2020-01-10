from bs4 import BeautifulSoup
import requests
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def sendmail(from_email, password, to_email, subject,  message):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, "plain"))
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, str(msg))
        server.close()
        return True
    except Exception as e:
        print("Something went wrong" + str(e))


def get_news():
    source = requests.get('https://az247.cz/').text
    soup = BeautifulSoup(source, 'lxml')
    news = [article.text for article in soup.find_all('div', class_='spotlight-item-caption')]
    return news


if __name__ == '__main__':
    file = open('kod', 'r')
    password = file.read()
    sendmail('python.analyssis@gmail.com', str(password), 'xdocad01@gjk.cz', 'hehehe', str(get_news()))
    file.close()




