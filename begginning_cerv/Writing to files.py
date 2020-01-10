
employee_file = open("employees", "a")
employee_name = input("Enter a name of the employee: ")
employee_activity = input("Enter the current job of the employee: ")

employee_file.write("\n" + employee_name + " - " + employee_activity)





employee_file.close()



