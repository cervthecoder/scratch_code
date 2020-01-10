

def register(nickname):
    file = open(nickname, "w")
    password = str(input("Enter your password: "))
    password_repeat = input("Re-enter your password: ")

    if password == password_repeat:
        file.write(password)
        print("You've had correctly entered you password")
        file.close

    else:
        print("You entered your password incorrectly")
        file.close()


def login(nickname):
    file = open(nickname, "r")
    password = str(input("Enter your password: "))
    read_password = file.readline()
    if password == read_password:
        print("You've logged correctly")
    else:
        print("Your password was inserted incorrectly")



choice = input("Do you want to register/login: ")

if choice == "register":
    nickname_1 = input("Enter your nickname: ")
    register(nickname_1)

elif choice == "login":
    nickname_2 = input("Enter your nickname: ")
    login(nickname_2)
























