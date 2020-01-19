def swap_case(s):
    return "".join([char.upper() if char.islower() else char.lower() for char in s])   

if __name__ == '__main__':
    print(swap_case("CBWHQd"))