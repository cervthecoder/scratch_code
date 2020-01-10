
def gen_primes(n):
    def gp(n):
        return [n[0]] + gp([i for i in n[1:] if i%n[0] != 0]) if n else []
    return gp(range(2,n))


def delitel_find(num):
    delitel = 2
    primes = gen_primes(num//2 + 1)
    numlist = []
    while delitel <= num:
        if (num % delitel) == 0 and delitel in primes:
            numlist.append(delitel)
            num = num//delitel
        else:
            delitel += 1

    return numlist

first = delitel_find(24)
second = delitel_find(58)
print(first, " ", second)


for n in first:
    if n in second:
        second.remove(n)
        first.remove(n)



print(first, " ", second)


