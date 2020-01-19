def dek(line):
    trantab = str.maketrans(" ", "-")
    return line.translate(trantab)

def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    return "".join(string)


