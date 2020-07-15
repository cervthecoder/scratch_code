from itertools import permutations

permuts = [''.join(p) for p in permutations('AAAABBBCC')]

perms = []

for item in permuts:
    if perms.count(item) == 0:
        perms.append(item)

count = 0
for i in perms:
    l = [n for n in i]
    index_l = 0
    for  n in l:
        if index_l == 8:
            count += 1
            break
        if n == l[index_l + 1]:
            break
        else:
            index_l+=1

print(count)


