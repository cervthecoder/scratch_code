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

subjects_1 = ["fy","bi","m", "zem", "ch", "čj", "hst", "udj", "tv", "dej", "ev", "sh", "inf", "aj", "fr"]


print("Now enter marks for physics")
marks_25_fy = str(input("Enter marks for 0.25: "))
marks_50_fy = str(input("Enter marks for 0.50: "))
marks_75_fy = str(input("Enter marks for 0.75: "))
marks_100_fy = str(input("Enter marks for 1.00: "))

print("Now enter marks for biology")
marks_25_bi = str(input("Enter marks for 0.25: "))
marks_50_bi = str(input("Enter marks for 0.50: "))
marks_75_bi = str(input("Enter marks for 0.75: "))
marks_100_bi = str(input("Enter marks for 1.00: "))

print("Now enter marks for mathematics")
marks_25_m = str(input("Enter marks for 0.25: "))
marks_50_m = str(input("Enter marks for 0.50: "))
marks_75_m = str(input("Enter marks for 0.75: "))
marks_100_m = str(input("Enter marks for 1.00: "))

print("Now enter marks for geography")
marks_25_zem = str(input("Enter marks for 0.25: "))
marks_50_zem = str(input("Enter marks for 0.50: "))
marks_75_zem = str(input("Enter marks for 0.75: "))
marks_100_zem = str(input("Enter marks for 1.00: "))

print("Now enter marks for chemistry")
marks_25_ch = str(input("Enter marks for 0.25: "))
marks_50_ch = str(input("Enter marks for 0.50: "))
marks_75_ch = str(input("Enter marks for 0.75: "))
marks_100_ch = str(input("Enter marks for 1.00: "))

print("Now enter marks for czech language")
marks_25_cj = str(input("Enter marks for 0.25: "))
marks_50_cj = str(input("Enter marks for 0.50: "))
marks_75_cj = str(input("Enter marks for 0.75: "))
marks_100_cj = str(input("Enter marks for 1.00: "))

print("Now enter marks for HST")
marks_25_hst = str(input("Enter marks for 0.25: "))
marks_50_hst = str(input("Enter marks for 0.50: "))
marks_75_hst = str(input("Enter marks for 0.75: "))
marks_100_hst = str(input("Enter marks for 1.00: "))

print("Now enter marks for UDJ")
marks_25_udj = str(input("Enter marks for 0.25: "))
marks_50_udj = str(input("Enter marks for 0.50: "))
marks_75_udj = str(input("Enter marks for 0.75: "))
marks_100_udj = str(input("Enter marks for 1.00: "))

print("Now enter marks for PE")
marks_25_tv = str(input("Enter marks for 0.25: "))
marks_50_tv = str(input("Enter marks for 0.50: "))
marks_75_tv = str(input("Enter marks for 0.75: "))
marks_100_tv = str(input("Enter marks for 1.00: "))

print("Now enter marks for history")
marks_25_dej = str(input("Enter marks for 0.25: "))
marks_50_dej = str(input("Enter marks for 0.50: "))
marks_75_dej = str(input("Enter marks for 0.75: "))
marks_100_dej = str(input("Enter marks for 1.00: "))

print("Now enter marks for EV")
marks_25_ev = str(input("Enter marks for 0.25: "))
marks_50_ev = str(input("Enter marks for 0.50: "))
marks_75_ev = str(input("Enter marks for 0.75: "))
marks_100_ev = str(input("Enter marks for 1.00: "))

marks_25_sh = str(input("Enter marks for 0.25: "))
marks_50_sh = str(input("Enter marks for 0.50: "))
marks_75_sh = str(input("Enter marks for 0.75: "))
marks_100_sh = str(input("Enter marks for 1.00: "))

print("Now enter marks for computers")
marks_25_inf = str(input("Enter marks for 0.25: "))
marks_50_inf = str(input("Enter marks for 0.50: "))
marks_75_inf = str(input("Enter marks for 0.75: "))
marks_100_inf = str(input("Enter marks for 1.00: "))

print("Now enter marks for english")
marks_25_aj = str(input("Enter marks for 0.25: "))
marks_50_aj = str(input("Enter marks for 0.50: "))
marks_75_aj = str(input("Enter marks for 0.75: "))
marks_100_aj = str(input("Enter marks for 1.00: "))

print("Now enter marks for french")
marks_25_fr = str(input("Enter marks for 0.25: "))
marks_50_fr = str(input("Enter marks for 0.50: "))
marks_75_fr = str(input("Enter marks for 0.75: "))
marks_100_fr = str(input("Enter marks for 1.00: "))

month = input("Enter the current month: ")

sendmail("python.analyssis@gmail.com", "Matej2003", "matej.cervenka03@gmail.com", month + " - Grades analyze", "Váha 0.25 fyzika " + marks_25_fy +"\n""Váha 0.50 fyzika " + marks_50_fy +"\n""Váha 0.75 fyzika " + marks_75_fy +"\n""Váha 1.0 fyzika " + marks_100_fy +"\n\n""Váha 0.25 biologie " + marks_25_bi +"\n""Váha 0.50 biologie " + marks_50_bi +"\n""Váha 0.75 biologie " + marks_75_bi +"\n""Váha 1.0 biologie " + marks_100_bi +"\n\n""Váha 0.25 matematika " + marks_25_m +"\n""Váha 0.50 matematika " + marks_50_m +"\n""Váha 0.75 matematika " + marks_75_m +"\n""Váha 1.0 matematika " + marks_100_m +"\n\n""Váha 0.25 zeměpis " + marks_25_zem +"\n""Váha 0.50 zeměpis " + marks_50_zem +"\n""Váha 0.75 zeměpis " + marks_75_zem +"\n""Váha 1.0 zeměpis " + marks_100_zem +"\n\n""Váha 0.25 chemie " + marks_25_ch +"\n""Váha 0.50 chemie " + marks_50_ch +"\n""Váha 0.75 chemie " + marks_75_ch +"\n""Váha 1.0 chemie " + marks_100_ch +"\n\n""Váha 0.25 český jazyk " + marks_25_cj +"\n""Váha 0.50 český jazyk " + marks_50_cj +"\n""Váha 0.75 český jazyk " + marks_75_cj +"\n""Váha 1.0 český jazyk " + marks_100_cj +"\n\n""Váha 0.25 HST " + marks_25_hst +"\n""Váha 0.50 HST " + marks_50_hst +"\n""Váha 0.75 HST " + marks_75_hst +"\n""Váha 1.0 HST " + marks_100_hst +"\n\n""Váha 0.25 UDJ " + marks_25_udj +"\n""Váha 0.50 UDJ " + marks_50_udj +"\n""Váha 0.75 UDJ " + marks_75_udj +"\n""Váha 1.0 UDJ " + marks_100_udj +"\n\n""Váha 0.25 tělesná výchova " + marks_25_tv +"\n""Váha 0.50 tělesná výchova " + marks_50_tv +"\n""Váha 0.75 tělesná výchova " + marks_75_tv +"\n""Váha 1.0 tělesná výchova " + marks_100_tv +"\n\n""Váha 0.25 dějepis " + marks_25_dej +"\n""Váha 0.50 dějepis " + marks_50_dej +"\n""Váha 0.75 dějepis " + marks_75_dej +"\n""Váha 1.0 dějepis " + marks_100_dej +"\n\n""Váha 0.25 etická výchova " + marks_25_ev +"\n""Váha 0.50 etická výchova " + marks_50_ev +"\n""Váha 0.75 etická výchova " + marks_75_ev +"\n""Váha 1.0 etická výchova " + marks_100_ev +"\n\n""Váha 0.25 SH " + marks_25_sh +"\n""Váha 0.50 SH " + marks_50_sh +"\n""Váha 0.75 SH " + marks_75_sh +"\n""Váha 1.0 SH " + marks_100_sh +"\n\n""Váha 0.25 informatika " + marks_25_inf +"\n""Váha 0.50 informatika " + marks_50_inf +"\n""Váha 0.75 informatika " + marks_75_inf +"\n""Váha 1.0 informatika " + marks_100_inf +"\n\n""Váha 0.25 anglický jazyk " + marks_25_aj +"\n""Váha 0.50 anglický jazyk " + marks_50_aj +"\n""Váha 0.75 anglický jazyk " + marks_75_aj +"\n""Váha 1.0 anglický jazyk " + marks_100_aj +"\n\n""Váha 0.25 francouzký jazyk " + marks_25_fr +"\n""Váha 0.50 francouzský jazyk " + marks_50_fr +"\n""Váha 0.75 francouzský jazyk " + marks_75_fr +"\n""Váha 1.0 francouzký jazyk " + marks_100_fr +"\n")
sendmail("python.analyssis@gmail.com", "Matej2003", "sona.cervenkova@gmail.com", month + " - Grades analyze", "Váha 0.25 fyzika " + marks_25_fy +"\n""Váha 0.50 fyzika " + marks_50_fy +"\n""Váha 0.75 fyzika " + marks_75_fy +"\n""Váha 1.0 fyzika " + marks_100_fy +"\n\n""Váha 0.25 biologie " + marks_25_bi +"\n""Váha 0.50 biologie " + marks_50_bi +"\n""Váha 0.75 biologie " + marks_75_bi +"\n""Váha 1.0 biologie " + marks_100_bi +"\n\n""Váha 0.25 matematika " + marks_25_m +"\n""Váha 0.50 matematika " + marks_50_m +"\n""Váha 0.75 matematika " + marks_75_m +"\n""Váha 1.0 matematika " + marks_100_m +"\n\n""Váha 0.25 zeměpis " + marks_25_zem +"\n""Váha 0.50 zeměpis " + marks_50_zem +"\n""Váha 0.75 zeměpis " + marks_75_zem +"\n""Váha 1.0 zeměpis " + marks_100_zem +"\n\n""Váha 0.25 chemie " + marks_25_ch +"\n""Váha 0.50 chemie " + marks_50_ch +"\n""Váha 0.75 chemie " + marks_75_ch +"\n""Váha 1.0 chemie " + marks_100_ch +"\n\n""Váha 0.25 český jazyk " + marks_25_cj +"\n""Váha 0.50 český jazyk " + marks_50_cj +"\n""Váha 0.75 český jazyk " + marks_75_cj +"\n""Váha 1.0 český jazyk " + marks_100_cj +"\n\n""Váha 0.25 HST " + marks_25_hst +"\n""Váha 0.50 HST " + marks_50_hst +"\n""Váha 0.75 HST " + marks_75_hst +"\n""Váha 1.0 HST " + marks_100_hst +"\n\n""Váha 0.25 UDJ " + marks_25_udj +"\n""Váha 0.50 UDJ " + marks_50_udj +"\n""Váha 0.75 UDJ " + marks_75_udj +"\n""Váha 1.0 UDJ " + marks_100_udj +"\n\n""Váha 0.25 tělesná výchova " + marks_25_tv +"\n""Váha 0.50 tělesná výchova " + marks_50_tv +"\n""Váha 0.75 tělesná výchova " + marks_75_tv +"\n""Váha 1.0 tělesná výchova " + marks_100_tv +"\n\n""Váha 0.25 dějepis " + marks_25_dej +"\n""Váha 0.50 dějepis " + marks_50_dej +"\n""Váha 0.75 dějepis " + marks_75_dej +"\n""Váha 1.0 dějepis " + marks_100_dej +"\n\n""Váha 0.25 etická výchova " + marks_25_ev +"\n""Váha 0.50 etická výchova " + marks_50_ev +"\n""Váha 0.75 etická výchova " + marks_75_ev +"\n""Váha 1.0 etická výchova " + marks_100_ev +"\n\n""Váha 0.25 SH " + marks_25_sh +"\n""Váha 0.50 SH " + marks_50_sh +"\n""Váha 0.75 SH " + marks_75_sh +"\n""Váha 1.0 SH " + marks_100_sh +"\n\n""Váha 0.25 informatika " + marks_25_inf +"\n""Váha 0.50 informatika " + marks_50_inf +"\n""Váha 0.75 informatika " + marks_75_inf +"\n""Váha 1.0 informatika " + marks_100_inf +"\n\n""Váha 0.25 anglický jazyk " + marks_25_aj +"\n""Váha 0.50 anglický jazyk " + marks_50_aj +"\n""Váha 0.75 anglický jazyk " + marks_75_aj +"\n""Váha 1.0 anglický jazyk " + marks_100_aj +"\n\n""Váha 0.25 francouzký jazyk " + marks_25_fr +"\n""Váha 0.50 francouzský jazyk " + marks_50_fr +"\n""Váha 0.75 francouzský jazyk " + marks_75_fr +"\n""Váha 1.0 francouzký jazyk " + marks_100_fr +"\n")


