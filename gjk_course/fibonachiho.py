def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return (F(n - 1) + F(n - 2))

def better_F(n):
    a = 1
    b = 1
    c = 1
    while c != n:
        a = a + b
        b = a + b
        c += 1

    if (n % 2) == 0:
        return b
    else:
        return a
print(better_F(20000))
