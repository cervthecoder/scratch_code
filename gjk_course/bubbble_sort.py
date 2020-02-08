l = [101, 66, 89, 99, 100, 38, 39]

i = 0
while i < len(l):
        for x in range(len(l) - 1):
            if l[x] > l[x + 1]:
                l[x], l[x + 1] = l[x + 1], l[x]
                i = 0
        i += 1

print(l)
