
employee_file = open("employees", "r")
# you can read the info from file by "r", with "w" you write into the file, with "a" you add on the end of the list, "r+" read and write
read_able = bool(employee_file.readable())

if read_able:
    print("You can read this file")

for employee in employee_file.readlines():
    print(employee)

employee_file.readline(1)




employee_file.close()



