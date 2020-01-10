import getpass
import smtplib
import random
import hashlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendmail(from_email, password, to_email, subject, message):
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


def register(username):
    file = open(username, "w")
    password = getpass.getpass("Enter your password: ")
    password_repeat = getpass.getpass("Reenter your password: ")

    if password == password_repeat:
        pass_hashed = hashlib.md5(str.encode(password)).hexdigest()
        file.write(str(pass_hashed))
        print("You've had correctly entered you password")
        file.close()
        file_2 = open(username, "a+")
        day_birth = str(input("What day is your birthday? (1, 23, 30...)"))
        month_birth = str(input("Which month is your birthday (february, january, may....)"))
        year_birth = input("What year you were born?(1973, 1999, 2004...)")
        file_2.write("\n" + day_birth + ". " + month_birth + " " + year_birth)
        height = str(input("Enter your height in centimeters: "))
        weight = str(input("Enter your weight in kilograms: "))
        file_2.write("\n Body stats" + height + "cm ," + weight + "kg")





    else:
        print("You entered your password incorrectly")
        file.close()


def login(username):
    file = open(username, "r+")
    password = getpass.getpass("Enter your password: ")
    pass_hashed = hashlib.md5(str.encode(password)).hexdigest()
    read_password = file.readline()
    if str(pass_hashed) == str(read_password):
        print("You've logged correctly")
        change_choice = input("Do you want to change your password? (yes/no): ")
        if change_choice == "yes":
            change_password = getpass.getpass("Enter your new password: ")
            change_password_repeat = getpass.getpass("Reenter your password: ")
            if change_password == change_password_repeat:
                change_password_hashed = hashlib.md5(str.encode(change_password)).hexdigest()
                file.write(str(change_password_hashed))
            else:
                print("You entered your password incorrectly")
        else:
            print("You don't want to change your password")
            file.close()
    else:
        print("Your password was inserted incorrectly")
        change_choice_2 = input("Do you want to re-verify your password?(yes/no): ")
        if change_choice_2 == "yes":
            email_user = input("Input your email for verification: ")
            message_random = random.randint(1, 100000000)
            sendmail("python.analyssis@gmail.com", "Matej2003", str(email_user), "Your password verification",
                     str(message_random))
            number_input = input("Enter the number you received in your mail: ")
            if str(message_random) == str(number_input):
                change_password = getpass.getpass("Enter your new password: ")
                change_password_repeat = getpass.getpass("Reenter your password: ")
                if change_password == change_password_repeat:
                    change_password_hashed = hashlib.md5(str.encode(change_password)).hexdigest()
                    file.write(change_password_hashed)
                    file.close()
                else:
                    print("You entered your password incorrectly")
            else:
                print("The number is not correct")
        else:
            print("You don't want to change you password")


choice = input("Do you want to register/login: ")

if choice == "register":
    username_1 = input("Enter your username: ")
    register(username_1)



elif choice == "login":
    username_2 = input("Enter your username: ")
    login(username_2)
