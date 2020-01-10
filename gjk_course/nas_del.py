from functools import reduce




def gen_primes(lim):
    return [i for i in reduce((lambda a, b: [(i[0] if i[0] == i[1] else 0) for i in zip(a, b)]), [[(0 if ((x % i == 0) and (x != i)) else x) for x in range(2, lim)] for i in range(2, lim)]) if i != 0]


def delitel_find(num):
    delitel = 2
    primes = gen_primes(int(num/2))
    numlist = []
    while delitel <= num:
        if num != delitel:
            if (num % delitel) == 0 and delitel in primes:
                numlist.append(delitel)
                if (num / delitel) % delitel == 0:
                    num = num / delitel
                elif (num / delitel) % delitel != 0:
                    delitel += 1
            elif (num % delitel) != 0:
                delitel += 1
        else:
            delitel += 1


    return numlist

x = int(input("Enter number: "))


print(delitel_find(x))










