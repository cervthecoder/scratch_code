input1 = input("Give the first number: ")
input2 = input("Give the second number: ")
input3 = input("Give the third number: ")


def max_num(num1, num2, num3):

    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3



print(max_num(float(input1),float(input2),float(input3)))


