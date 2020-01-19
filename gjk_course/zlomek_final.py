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



class Zlomek:
    def __init__(self, čitatel, jmenovatel):
        self.čitatel = čitatel
        self.jmenovatel = jmenovatel

    def ukaž(self):
        print(f'{self.čitatel} \n{"".join([ "-" for digits in range(len((str(self.jmenovatel))))])} \n{self.jmenovatel}\n')

    def vrať_list(self):
        return [self.čitatel, self.jmenovatel]

    def vynásob(self, other):
        l = vyhoď_základnítvar_upravené(self.čitatel, self.jmenovatel, other.čitatel, other.jmenovatel)
        fin = základní_tvar(l[0]*l[2], l[1]*l[3])
        return Zlomek(fin[0], fin[1])

    def vyděl(self, other):
        l = vyhoď_základnítvar_upravené(self.čitatel, self.jmenovatel, other.čitatel, other.jmenovatel)
        fin = základní_tvar(l[0]*l[3], l[1]*l[2])
        return Zlomek(fin[0], fin[1])

    def sečti(self, other):
        l = vyhoď_základnítvar_upravené(self.čitatel, self.jmenovatel, other.čitatel, other.jmenovatel)
        fin =  základní_tvar(l[0]*l[3] + l[2]*l[1], l[1]*l[3])   
        return Zlomek(fin[0], fin[1])

    def odečti(self, other):
        l = vyhoď_základnítvar_upravené(self.čitatel, self.jmenovatel, other.čitatel, other.jmenovatel)
        fin = základní_tvar(l[0]*l[3] - l[2]*l[1], l[1]*l[3])  
        return Zlomek(fin[0], fin[1])

    def __add__(self, other):
        return self.sečti(other)

    def __sub__(self, other):
        return self.odečti(other)

    def __mul__(self, other):
        return self.vynásob(other)

    def __truediv__(self, other):
        return self.vyděl(other)

if '__main__' == __name__:

    zlomek = Zlomek(65,9)
    zlomek_1 = Zlomek(76,8)

    new_zlomek = (zlomek_1 + zlomek)

    new_zlomek.ukaž()

    (zlomek_1 * zlomek).ukaž()

    print(zlomek.vrať_list())


    






