import smtplib
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


month = input("Enter the current month")

sendmail("python.analyssis@gmail.com", "Matej2003", "matej.cervenka03@gmail.com", month + " - Grades analyze","")
