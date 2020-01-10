x = float(input("Enter a number:"))
y = x
end = int(input("Enter an exponent: "))


for i in range(1, end):
    x = y * x

print(x)