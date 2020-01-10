def gen_primes(n):
    def gp(n):
        return [n[0]] + gp([i for i in n[1:] if i%n[0] != 0]) if n else []
    return gp(range(2,n))


end = int(input())
i = 0

for n in gen_primes(end + 1):
    i += 1


print(i)



