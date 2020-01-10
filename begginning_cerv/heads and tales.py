import random



coins = int(input("Enter the number of coins, you want to be thrown: "))

heads = 0
tales = 0

x = 0

for x in range(1, coins):
    x = random.randint(1, 2)
    if x = 1:
        heads += 1

    elif x = 2:
       tales += 1

print(heads)
print(tales)