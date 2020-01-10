grid = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]


]

x = False

taken_positions = ["[1][1]", "[1][2]", "[1][2]", "[2][2]", "[3][2]", "[1][3]", "[2][3]", "[3][3]", "[1][1]"]


def lock_position_1():
    global x_input_1
    global y_input_1
    global taken_positions
    if ("[" + x_input_1 + "]" + "[" + y_input_1 + "]") not in taken_positions:
        taken_positions.append("[" + x_input_1 + "]" + "[" + y_input_1 + "]")

    else:
        pass


def lock_positions_2():
    global x_input_2
    global y_input_2
    global taken_positions

    if ("[" + x_input_2 + "]" + "[" + y_input_2 + "]") not in taken_positions:
        taken_positions.append("[" + x_input_2 + "]" + "[" + y_input_2 + "]")
    else:
        pass



def play1():
    global taken_positions
    global x_input_1
    global y_input_1
    global form
    true_x = False
    true_y = False
    print("Now will play player 1")

    while ("[" + str(x_input_1) + "]" + "[" + str(y_input_1) + "]") in taken_positions:


        while not true_x:
            x_input_1 = int(input("Enter x axis position (1, 2, 3): "))


            if int(x_input_1) == 1:
                true_x = True
            elif int(x_input_1) == 2:
                true_x = True
            elif int(x_input_1) == 3:
                true_x = True

            else:
                print("Try again (1, 2, 3)")

        while not true_y:
            y_input_1 = int(input("Enter y axis position (1, 2, 3): "))

            if int(y_input_1) == 1:
                true_y = True
            elif int(y_input_1) == 2:
                true_y = True
            elif int(y_input_1) == 3:
                true_y = True
            else:
                print("Try again (1, 2, 3)")
        print("That position is taken")






    grid[int(x_input_1) - 1][int(y_input_1) - 1] = "X"

    print(grid[0][0] + "  |  " + grid[1][0] + "  |  " + grid[2][0] + "\n" + "__" + "   " + "__" + "   " + "__" +
          "\n" + grid[0][1] + "   |  " + grid[1][1] + "  |  " + grid[2][1] + "\n" + "__" + "   " + "__" + "   " + "__" +
          "\n" + grid[0][2] + "   |  " + grid[1][2] + "  |  " + grid[2][2])






def play2():
    print("Now will play player 2\n")
    global x_input_2
    global y_input_2
    true_x_1 = False
    true_y_1 = False

    while ("[" + str(x_input_2) + "]" + "[" + str(y_input_2) + "]") in taken_positions:

        while not true_x_1:
            x_input_2 = int(input("Enter x axis position (1, 2, 3): "))

            if int(x_input_2) == 1:
                true_x_1 = True
            elif int(x_input_2) == 2:
                true_x_1 = True
            elif int(x_input_2) == 3:
                true_x_1 = True
            else:
                print("Try again (1, 2, 3)")

        while not true_y_1:
            y_input_2 = int(input("Enter y axis position (1, 2, 3): "))

            if int(y_input_2) == 1:
                true_y_1 = True
            elif int(y_input_2) == 2:
                true_y_1 = True
            elif int(y_input_2) == 3:
                true_y_1 = True
            else:
                print("Try again (1, 2, 3)")

    print("That position is taken")

    grid[x_input_2 - 1][y_input_2 - 1] = "O"

    print(grid[0][0] + "  |  " + grid[1][0] + "  |  " + grid[2][0] + "\n" + "__" + "   " + "__" + "   " + "__" +
          "\n" + grid[0][1] + "   |  " + grid[1][1] + "  |  " + grid[2][1] + "\n" + "__" + "   " + "__" + "   " + "__" +
          "\n" + grid[0][2] + "   |  " + grid[1][2] + "  |  " + grid[2][2])


def win():
    global x
    x0_y0 = grid[0][0]
    x0_y1 = grid[0][1]
    x0_y2 = grid[0][2]
    x1_y0 = grid[1][0]
    x1_y1 = grid[1][1]
    x1_y2 = grid[1][2]
    x2_y0 = grid[2][0]
    x2_y1 = grid[2][1]
    x2_y2 = grid[2][2]

    if x0_y0 == x0_y1 == x0_y2 and x0_y0 == "X":
        print("Player 1 wins")
        x = True

    elif x1_y0 == x1_y1 == x1_y2 and x1_y0 == "X":
        print("Player 1 wins")
        x = True
    elif x2_y0 == x2_y1 == x2_y2 and x2_y0 == "X":
        print("Player 1 wins")
        x = True
    elif x0_y0 == x1_y0 == x2_y0 and x0_y0 == "X":
        print("Player 1 wins")
        x = True
    elif x0_y1 == x1_y1 == x0_y2 and x0_y1 == "X":
        print("Player 1 wins")
        x = True
    elif x0_y2 == x1_y2 == x2_y2 and x0_y2 == "X":
        print("Player 1 wins")
        x = True
    elif x0_y0 == x1_y1 == x2_y2 and x0_y0 == "X":
        print("Player 1 wins")
        x = True
    elif x2_y0 == x1_y1 == x0_y2 and x2_y0 == "X":
        print("Player 1 wins")
        x = True



    elif x0_y0 == x0_y1 == x0_y2 and x0_y0 == "O":
        print("Player 2 wins")
        x = True
    elif x1_y0 == x1_y1 == x1_y2 and x1_y0 == "O":
        print("Player 2 wins")
        x = True
    elif x2_y0 == x2_y1 == x2_y2 and x2_y0 == "O":
        print("Player 2 wins")
        x = True
    elif x0_y0 == x1_y0 == x2_y0 and x0_y0 == "O":
        print("Player 2 wins")
        x = True
    elif x0_y1 == x1_y1 == x0_y2 and x0_y1 == "O":
        print("Player 2 wins")
        x = True
    elif x0_y2 == x1_y2 == x2_y2 and x0_y2 == "O":
        print("Player 2 wins")
        x = True
    elif x0_y0 == x1_y1 == x2_y2 and x0_y0 == "O":
        print("Player 2 wins")
        x = True
    elif x2_y0 == x1_y1 == x0_y2 and x2_y0 == "O":
        print("Player 2 wins")
        x = True



while not x:
    win()
    play1()
    lock_position_1()

    win()
    if not x:
        play2()
        lock_positions_2()

print("End of the game")
