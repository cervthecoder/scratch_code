from sys import stdout as st



def phone(number):
    num_list = []
    first = ["+", "91", " "]
    last = [" "]
    final = []

    for digit in number:
        num_list.append(digit)
    for dig in num_list[0:4]:
        first.append(dig)
    for dig1 in num_list[4:9]:
        last.append(dig1)
        print("hihi")


        first += last
        final += first

        return final
    print(num_list[4:9])



if __name__ == '__main__':
    for char in phone("1234567890"):
        st.write(char)




