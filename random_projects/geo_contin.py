from itertools import permutations

permuts = [''.join(p) for p in permutations('AAAABBBCC')]
count = 0
for i in permuts:
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

count = 0

for per in permuts:
    print(per)
    count += 1


print(count)




