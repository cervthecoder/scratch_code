if __name__ == '__main__':
    N = int(input())
    list_1 = []
    for e in range(N):
        i = input()
        if "insert" in i:
            pos_insert = [pos for pos in i if pos.isnumeric() or pos == " "]
            for char in pos_insert:
                if char.isnumeric():
                     if pos_insert[(char.index() + 1)] == " ":
                        break
                     else:
                         pass


            #list_1.insert(pos_insert[0], pos_insert[1])
        elif i == "print":
            print(list_1)
        elif "remove" in i:
            pos_remove = [int(pos) for pos in i if pos.isnumeric()]
            list_1.remove(pos_remove[0])
        elif "append" in i:
            pos_append = [int(pos) for pos in i if pos.isnumeric()]
            list_1.append(pos_append[0])
        elif i == "sort":
            list_1.sort()
        elif i == "pop":
            list_1.pop()
        elif i == "reverse":
            list_1.reverse()

