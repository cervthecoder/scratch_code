
num1 = float(input("Enter 1st number: "))
operator = input("+, -, /, *, ^, bin: ")
num2 = float(input("Enter 2nd number: "))

if operator == "+":
    print(num1+num2)

elif operator == "-":
    print(num1-num2)

elif operator == "/":
    print(num1/num2)

elif operator == "*":
    print(num1*num2)

elif operator == "^":
    print(num1**num2)

elif operator == "bin":
    print(str(bin(int(num1)))+ " first number in binary")
    print(str(bin(int(num2)))+ " second number in binary")
else:
    print("invalid operator")











