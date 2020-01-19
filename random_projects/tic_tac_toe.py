def grid():
    return [["   _" for column in range(3)] for row in range(3)]

def print_grid(the_grid):
    for row in the_grid:
        print("".join(row))
        print('\n')

def format_input():
    l_form = [int(char) for char in str_input if char.isdigit()]
    return [l_form[0],l_form[1]]

def replace_in_grid(the_grid ,row, column, char):
    the_grid[row][column] = f'   {char}'

def player_play(the_grid, row, column, char): # input is like "x y"
    while is_taken(the_grid, row, column):
        str_input = input("Enter the coordinates(row column)")
    replace_in_grid(the_grid, [int(char) for char in str_input if char.isdigit()][0],[int(char) for char in str_input if char.isdigit()][1] , char)

def is_taken(the_grid, row, column):
    if the_grid[row][column] in ("   X", "   O"):
        return True

def isend(the_grid):
    while not is_row_win(the_grid) or not is_column_win(the_grid) or not is_diagonal_win(the_grid):
        return False
    print_grid("The game ends")
    return True

def is_row_win(the_grid):
    winning_row_x = ["   X" for _ in range(3)]
    winning_row_o = ["   0" for _ in range(3)]
    for n in range(2):
        if the_grid[n] in (winning_row_o, winning_row_x):
            return True
        else:
            return False

def is_column_win(the_grid):
    rotated_grid = zip(*my_grid[::-1])
    winning_col_x = ["   X" for _ in range(3)]
    winning_col_o = ["   0" for _ in range(3)]
    for n in range(3):
        if the_grid[n] in (winning_col_o, winning_col_x):
            return True
        else:
            return False

def is_diagonal_win(the_grid):
    winning_dia_x = ["   X" for _ in range(2)]
    winning_dia_o = ["   0" for _ in range(2)]
    diagonal_1 = []
    diagonal_2 = []
    for n in range(1,3):
        diagonal_1.append(the_grid[n][n])
        diagonal_2.append(the_grid[n][2 - n])
    if diagonal_1 in (winning_dia_o, winning_dia_x) or diagonal_2 in (winning_dia_x, winning_dia_o):
        return True
    else:
        return False

def main(the_grid):
    while not isend(the_grid):
        str_input = input("player_1 enter the coordinates(row column)")
        player_play(the_grid, format_input(str_input)[0], format_input(str_input)[1], "X")
        print_grid(the_grid)
        str_input = input("player_1 enter the coordinates(row column)")
        player_play(the_grid, format_input(str_input)[0], format_input(str_input)[1], "0")
        print_grid(the_grid)

if __name__ == '__main__':
    main(grid())





    









