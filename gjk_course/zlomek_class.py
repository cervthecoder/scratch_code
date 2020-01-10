import numpy as np


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

def základní_tvar(čitatel, jmenovatel):
    jmen = delitel_find(jmenovatel)
    čit = delitel_find(čitatel)
    for n in čit:
        if n in jmen:
            jmen.remove(n)
            čit.remove(n)

    return [np.prod(čit), np.prod(jmen)]



class zlomek:
    def __init__(self, čitatel, jmenovatel):
        self.čitatel = čitatel
        self.jmenovatel = jmenovatel


    def vynásob(self, druhý_čitatel, druhý_jmenovatel):
        čit_self = základní_tvar(self.čitatel, self.jmenovatel)[0]
        jmen_self = základní_tvar(self.čitatel, self.jmenovatel)[1]
        čit_2 = základní_tvar(druhý_čitatel, druhý_jmenovatel)[0]
        jmen_2 = základní_tvar(druhý_čitatel, druhý_jmenovatel)[1]
        
        return základní_tvar(čit_self*čit_2, jmen_self*jmen_2)

    def vyděl(self, druhý_čitatel, druhý_jmenovatel):
        čit_self = základní_tvar(self.čitatel, self.jmenovatel)[0]
        jmen_self = základní_tvar(self.čitatel, self.jmenovatel)[1]
        čit_2 = základní_tvar(druhý_čitatel, druhý_jmenovatel)[0]
        jmen_2 = základní_tvar(druhý_čitatel, druhý_jmenovatel)[1]

        return základní_tvar(čit_self*jmen_2, jmen_self*čit_2)

    def sečti(self, druhý_čitatel, druhý_jmenovatel):
        čit_self = základní_tvar(self.čitatel, self.jmenovatel)[0]
        jmen_self = základní_tvar(self.čitatel, self.jmenovatel)[1]
        čit_2 = základní_tvar(druhý_čitatel, druhý_jmenovatel)[0]
        jmen_2 = základní_tvar(druhý_čitatel, druhý_jmenovatel)[1]

        return základní_tvar(čit_self*jmen_2 + čit_2*jmen_self, jmen_self*jmen_2)

    def odečti(self, druhý_čitatel, druhý_jmenovatel):
        čit_self = základní_tvar(self.čitatel, self.jmenovatel)[0]
        jmen_self = základní_tvar(self.čitatel, self.jmenovatel)[1]
        čit_2 = základní_tvar(druhý_čitatel, druhý_jmenovatel)[0]
        jmen_2 = základní_tvar(druhý_čitatel, druhý_jmenovatel)[1]

        return základní_tvar(čit_self*jmen_2 - čit_2*jmen_self, jmen_self*jmen_2)

zlomek = zlomek(42, 55)

print(zlomek.vynásob(15, 68))
print(zlomek.vyděl(15, 68))
print(zlomek.sečti(24, 25))
print(zlomek.odečti(84, 15))



