# ©Matěj Červenka, ZLOMEK_OO, ALL RIGHTS RESERVED
import numpy as np


def gen_primes(n):
    def gp(n):
        return [n[0]] + gp([i for i in n[1:] if i%n[0] != 0]) if n else []
    return gp(range(2, int(n)))

def delitel_find(num):
    negative = False
    delitel = 2
    numlist = []
    if num < 0:
        num *= -1
        negative = True
    primes = gen_primes(num//2 + 1)
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

def vyhoď_základnítvar_upravené(čitatel_1, jmenovatel_1, čitatel_2, jmenovatel_2):
    return[základní_tvar(čitatel_1, jmenovatel_1)[0], základní_tvar(čitatel_1, jmenovatel_1)[1], základní_tvar(čitatel_2, jmenovatel_2)[0],základní_tvar(čitatel_2, jmenovatel_2)[1]]



class zlomek:
    def __init__(self, čitatel, jmenovatel):
        self.čitatel = čitatel
        self.jmenovatel = jmenovatel


    def vynásob(self, druhý_čitatel, druhý_jmenovatel):
        l = vyhoď_základnítvar_upravené(self.čitatel, self.jmenovatel, druhý_čitatel, druhý_jmenovatel)
        return základní_tvar(l[0]*l[2], l[1]*l[3])

    def vyděl(self, druhý_čitatel, druhý_jmenovatel):
        l = vyhoď_základnítvar_upravené(self.čitatel, self.jmenovatel, druhý_čitatel, druhý_jmenovatel)
        return základní_tvar(l[0]*l[3], l[1]*l[2])

    def sečti(self, druhý_čitatel, druhý_jmenovatel):
        l = vyhoď_základnítvar_upravené(self.čitatel, self.jmenovatel, druhý_čitatel, druhý_jmenovatel)    
        return základní_tvar(l[0]*l[3] + l[2]*l[1], l[1]*l[3])

    def odečti(self, druhý_čitatel, druhý_jmenovatel):
        l = vyhoď_základnítvar_upravené(self.čitatel, self.jmenovatel, druhý_čitatel, druhý_jmenovatel)    
        return základní_tvar(l[0]*l[3] - l[2]*l[1], l[1]*l[3])

zlomek = zlomek(42, 55)

print(zlomek.vynásob(15, 28))
print(zlomek.vyděl(15, 68))
print(zlomek.sečti(24, 25))
print(zlomek.odečti(84, 15))



