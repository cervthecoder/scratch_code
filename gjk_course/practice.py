# Enter your code here. Read input from STDIN. Print output to STDOUT


from sys import stdout as st
string = input("Enter your argument")
lower = []
upper = []
odd = []
even = []
final = []

for char in string:
    if char.isalpha():
        if char.islower():
            lower.append(char)
        elif char.isupper():
            upper.append(char)
    elif char.isdigit():
        if (int(char) % 2) != 0:
            odd.append(char)
        else:
            even.append(char)

lower.sort()
upper.sort()

for l in lower:
    final.append(l)

for L in upper:
    final.append(L)


for o in odd:
    final.append(o)

for e in even:
    final.append(e)


for let_dig in final:
    st.write(let_dig)
