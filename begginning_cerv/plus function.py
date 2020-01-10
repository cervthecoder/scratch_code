
num_1 = float(input("Enter your first number: "))
num_2 = float(input("Enter the second number: "))

choice = input("Enter the operation(+, -, /, *, **, %):  ")

if choice == "+":
    result_1 = float(num_1 + num_2 + 1)
    print(result_1)

elif choice == "-":
    result_2 = float(num_1 - num_2 - 1)
    print(result_2)

elif choice == "*":
    print(num_1 * num_2 * 3)

elif choice == "/":
    print(int(num_1 / num_2) + 69)

else:
    print(73)
