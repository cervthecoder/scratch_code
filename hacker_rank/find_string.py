from functools import reduce

def count_substring(string, sub_string):
    count = 0
    loop = 0
    stripped = [char for char in string if not char in [ch for ch in string.strip(sub_string)]]
    print(stripped)
    




if __name__ == '__main__':
    print(count_substring('GHCDABCDFGCD', 'CD'))
