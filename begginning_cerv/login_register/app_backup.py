import getpass
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Any, Union


def sendmail(from_email, password_e, to_email, subject, message):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, "plain"))
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(from_email, password_e)
        server.sendmail(from_email, to_email, str(msg))
        server.close()
        return True
    except Exception as e:
        print("Something went wrong" + str(e))

choice_lg = input("Do you want to login or register?: ")


if choice_lg == "register":
    username_r = input("Choose your username: ")
    file = open(username_r, "w")
    password = getpass.getpass("Enter your password: ")
    password_repeat = getpass.getpass("Re-enter your password: ")

    if str(password) == str(password_repeat):
        
        file.write(str(password))
        print("You've had correctly entered you password")
        file.close()
        file_2 = open(username_r, "a+")
        day_birth = str(input("What day is your birthday? (1, 23, 30...)"))
        month_birth = str(input("Which month is your birthday (february, january, may....)"))
        year_birth = input("What year you were born?(1973, 1999, 2004...)")
        file_2.write("\n" + day_birth + ". " + month_birth.capitalize() + " " + year_birth)
        height = str(input("Enter your height in centimeters: "))
        weight = str(input("Enter your weight in kilograms: "))
        file_2.write("\n Body stats- " + height + "cm ," + weight + "kg")
        functions_choice = input("Do you want to access any functions?(yes/no): ")
        if functions_choice == "yes":
            chosen_function = input("calculator, bricks")
        else:
            print("You've left the code")

    else:
        print("You entered your password incorrectly")
        file.close()


if choice_lg == "login":
    username_l = input("Enter your username: ")
    file_1 = open(username_l, "r+")
    read_password_1 = file_1.readline()
    print(read_password_1)
    out_of_passwords = False
    password_count = 0
    password_limit = 5
    password_l = getpass.getpass("Enter your password: ")

    
    
    while password_l != read_password_1 and out_of_passwords is False:

        if password_count <= password_limit:
            password_l = getpass.getpass("Enter your password: ")
            
            password_count += 1



        else:
            out_of_passwords = True
            change_choice = input("Do you want to change your password? (yes/no): ")
            if str(change_choice) == "yes":

                email_user = input("Input your email for verification: ")
                message_random: Union[int, Any] = random.randint(1, 100000000)
                sendmail("python.analyssis@gmail.com", "Matej2003", str(email_user), "Your password verification", str(message_random))
                number_input = input("Enter the number you received in your mail: ")
                if str(message_random) == str(number_input):
                    change_password = getpass.getpass("Enter your new password: ")
                    change_password_repeat = getpass.getpass("Reenter your password: ")
                    if change_password == change_password_repeat:
                        
                        file_1.write(change_password_repeat)
                        file_1.close()
                    else:
                        print("You repeated password incorrectly")
                else:
                    print("The number is wrong")




if password_l == read_password_1:
    print("You've accessed profile " + username_l)
    print(read_password_1)
    choice_l = input("Do you want to access any function?(yes/no): ")
    if str(choice_l) == "yes":
         function_choice_l = input("1.- Calculator \n2.- Throw number cubes")

