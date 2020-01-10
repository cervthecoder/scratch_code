import hashlib

password = input("Enter password: ")
hashed_password = hashlib.md5(str.encode(password)).hexdigest()
password2 = input("Enter your password: ")
hashed_password_2 = hashlib.md5(str.encode(password2)).hexdigest()
if hashed_password == hashed_password_2:
    print("Password is correct")
else:
    print("Password is wrong")


print(hashed_password)

