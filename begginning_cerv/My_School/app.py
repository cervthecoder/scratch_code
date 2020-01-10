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

restart = "yes"
subject1 = input("Choose subject (" + str(subjects_1) + ")")

def main():
    if subject1 == "fy":
        print("Now enter marks for physics")
        marks_25_fy = str(input("Enter marks for 0.25: "))
        marks_50_fy = str(input("Enter marks for 0.50: "))
        marks_75_fy = str(input("Enter marks for 0.75: "))
        marks_100_fy = str(input("Enter marks for 1.00: "))
        restart_str = str(input("Do you want to insert new marks?(yes/no)"))
        if restart_str == restart:
            main()
        else:
            exit()



    elif subject1 == "bi":
        print("Now enter marks for biology")
        marks_25_bi = str(input("Enter marks for 0.25: "))
        marks_50_bi = str(input("Enter marks for 0.50: "))
        marks_75_bi = str(input("Enter marks for 0.75: "))
        marks_100_bi = str(input("Enter marks for 1.00: "))
        restart_str = str(input("Do you want to insert new marks?(yes/no)"))
        if restart_str == restart:
            main()
        else:
            exit()

    elif subject1 == "m":
        print("Now enter marks for mathematics")
        marks_25_m = str(input("Enter marks for 0.25: "))
        marks_50_m = str(input("Enter marks for 0.50: "))
        marks_75_m = str(input("Enter marks for 0.75: "))
        marks_100_m = str(input("Enter marks for 1.00: "))
        restart_str = str(input("Do you want to insert new marks?(yes/no)"))
        if restart_str == restart:
            main()
        else:
            exit()

    elif subject1 == "zem":
        print("Now enter marks for geography")
        marks_25_zem = str(input("Enter marks for 0.25: "))
        marks_50_zem = str(input("Enter marks for 0.50: "))
        marks_75_zem = str(input("Enter marks for 0.75: "))
        marks_100_zem = str(input("Enter marks for 1.00: "))
        restart_str = str(input("Do you want to insert new marks?(yes/no)"))
        if restart_str == restart:
            main()
        else:
            exit()

    elif subject1 == "ch":
        print("Now enter marks for chemistry")
        marks_25_ch = str(input("Enter marks for 0.25: "))
        marks_50_ch = str(input("Enter marks for 0.50: "))
        marks_75_ch = str(input("Enter marks for 0.75: "))
        marks_100_ch = str(input("Enter marks for 1.00: "))
        restart_str = str(input("Do you want to insert new marks?(yes/no)"))
        if restart_str == restart:
            main()
        else:
            exit()

    elif subject1 == "čj":
        print("Now enter marks for czech language")
        marks_25_cj = str(input("Enter marks for 0.25: "))
        marks_50_cj = str(input("Enter marks for 0.50: "))
        marks_75_cj = str(input("Enter marks for 0.75: "))
        marks_100_cj = str(input("Enter marks for 1.00: "))
        restart_str = str(input("Do you want to insert new marks?(yes/no)"))
        if restart_str == restart:
            main()
        else:
            exit()

    elif subject1 == "hst":
        print("Now enter marks for HST")
        marks_25_hst = str(input("Enter marks for 0.25: "))
        marks_50_hst = str(input("Enter marks for 0.50: "))
        marks_75_hst = str(input("Enter marks for 0.75: "))
        marks_100_hst = str(input("Enter marks for 1.00: "))
        restart_str = str(input("Do you want to insert new marks?(yes/no)"))
        if restart_str == restart:
            main()
        else:
            exit()

    elif subject1 == "udj":
        print("Now enter marks for UDJ")
        marks_25_udj = str(input("Enter marks for 0.25: "))
        marks_50_udj = str(input("Enter marks for 0.50: "))
        marks_75_udj = str(input("Enter marks for 0.75: "))
        marks_100_udj = str(input("Enter marks for 1.00: "))
        restart_str = str(input("Do you want to insert new marks?(yes/no)"))
        if restart_str == restart:
            main()
        else:
            exit()

    elif subject1 == "tv":
        print("Now enter marks for PE")
        marks_25_tv = str(input("Enter marks for 0.25: "))
        marks_50_tv = str(input("Enter marks for 0.50: "))
        marks_75_tv = str(input("Enter marks for 0.75: "))
        marks_100_tv = str(input("Enter marks for 1.00: "))
        restart_str = str(input("Do you want to insert new marks?(yes/no)"))
        if restart_str == restart:
            main()
        else:
            exit()

    elif subject1 == "dej":
        print("Now enter marks for history")
        marks_25_dej = str(input("Enter marks for 0.25: "))
        marks_50_dej = str(input("Enter marks for 0.50: "))
        marks_75_dej = str(input("Enter marks for 0.75: "))
        marks_100_dej = str(input("Enter marks for 1.00: "))
        restart_str = str(input("Do you want to insert new marks?(yes/no)"))
        if restart_str == restart:
            main()
        else:
            exit()

    elif subject1 == "ev":
        print("Now enter marks for EV")
        marks_25_ev = str(input("Enter marks for 0.25: "))
        marks_50_ev = str(input("Enter marks for 0.50: "))
        marks_75_ev = str(input("Enter marks for 0.75: "))
        marks_100_ev = str(input("Enter marks for 1.00: "))
        restart_str = str(input("Do you want to insert new marks?(yes/no)"))
        if restart_str == restart:
            main()
        else:
            exit()

    elif subject1 == "sh":
        print("Now enter marks for SH")
        marks_25_sh = str(input("Enter marks for 0.25: "))
        marks_50_sh = str(input("Enter marks for 0.50: "))
        marks_75_sh = str(input("Enter marks for 0.75: "))
        marks_100_sh = str(input("Enter marks for 1.00: "))
        restart_str = str(input("Do you want to insert new marks?(yes/no)"))
        if restart_str == restart:
            main()
        else:
            exit()

    elif subject1 == "inf":
        print("Now enter marks for computers")
        marks_25_inf = str(input("Enter marks for 0.25: "))
        marks_50_inf = str(input("Enter marks for 0.50: "))
        marks_75_inf = str(input("Enter marks for 0.75: "))
        marks_100_inf = str(input("Enter marks for 1.00: "))
        restart_str = str(input("Do you want to insert new marks?(yes/no)"))
        if restart_str == restart:
            main()
        else:
            exit()

    elif subject1 == "aj":
        print("Now enter marks for english")
        marks_25_aj = str(input("Enter marks for 0.25: "))
        marks_50_aj = str(input("Enter marks for 0.50: "))
        marks_75_aj = str(input("Enter marks for 0.75: "))
        marks_100_aj = str(input("Enter marks for 1.00: "))
        restart_str = str(input("Do you want to insert new marks?(yes/no)"))
        if restart_str == restart:
            main()
        else:
            exit()

    elif subject1 == "fr":
        print("Now enter marks for french")
        marks_25_fr = str(input("Enter marks for 0.25: "))
        marks_50_fr = str(input("Enter marks for 0.50: "))
        marks_75_fr = str(input("Enter marks for 0.75: "))
        marks_100_fr = str(input("Enter marks for 1.00: "))
        restart_str = str(input("Do you want to insert new marks?(yes/no)"))
        if restart_str == restart:
            main()
        else:
            exit()

    else:
        print("Invalid input")
        restart_str = str(input("Do you want to insert new marks?(yes/no)"))
        if restart_str == restart:
            main()
        else:
            exit()

main()

month = input("Enter the current month")

sendmail("python.analyssis@gmail.com", "Matej2003", "matej.cervenka03@gmail.com", month + " - Grades analyze", mark_25_fy)









