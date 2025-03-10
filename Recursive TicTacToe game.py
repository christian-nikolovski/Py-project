global Variable

Variable = 1

#Imports
import copy
import sys
import os
import subprocess
import operator
import random
import time 
from colorama import Fore, Style

print(Style.BRIGHT)

#Clears the screen
def clear():
    print("\033[H\033[J") 

def Recursive_Tictactoe(): 
    #Global declarations
    global current_player
    global smol_board
    global winvalue
    global full_board_check
    global loop_of_full
    global coordinate
    global fullvalue
    global bigboard
    global full_board
    global infiloop
    global loop_of_game
    global same_winvalue
    global Variable_ender
    global not_valid
    global x
    global u 
    global list_of_full
    global dash_colour
    global First_Setup
    global EMPTY
    global one_list
    global X_colour
    global O_colour
    global Ø_colour
    global row_check
    global bigboard
    global board
    global better_board
    global loop_run_list
    global bigboard_values
    global smol_box
    global list_of_full
    global coordinate

    #String variables
    EMPTY = "-"
    N = " "
    current_player = "X"
    x = "│"
    u = "│ "
    one_list = "────────────────────┼─────────────────────┼────────────────────"
    X_colour = Fore.RED + "  │  "
    Ø_colour = Fore.GREEN + "  │  "
    O_colour = Fore.BLUE + "  │  "
    dash_colour = Fore.WHITE + "  │  "

    #Numerical variables
    First_Setup = 1
    full_board = 1
    infiloop = 1
    not_valid = 1 
    same_winvalue = 0
    row_check = 0
    Variable_ender = 0

    #Boolean variables
    loop_of_full = True
    loop_of_game = True

    #List variables
    bigboard = []
    board = []
    better_board = []
    loop_run_list = []
    bigboard_values = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    smol_box = ["────┼─────┼────", "────┼─────┼────", "────┼─────┼────", "────┼─────┼────", "────┼─────┼────", "────┼─────┼────", "────┼─────┼────", "────┼─────┼────", "────┼─────┼────"]
    list_of_full = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    #Dictionaries 
    columns = {"a": 0, "b": 1, "c": 2}
    rows = {"1": 0, "2": 1, "3": 2}
    columns_ai = {0: "a", 1: "b", 2: "c"}
    rows_ai = {0: "1", 1: "2", 2: "3"}
    smol_board_dict = {"a1": 0, "a2": 1, "a3": 2, "b1": 3, "b2": 4, "b3": 5, "c1": 6, "c2": 7, "c3": 8}

    #Make the list for the board
    for i in range(3):
        board.append([EMPTY, EMPTY, EMPTY])

    for i in range(9):
        bigboard.append(copy.deepcopy(board))

    # ______ to ______
    def dash_to_box():
        for t in range(3):
            for j in range(3):
                if smol_board[t][j] == "-":
                    smol_board[t][j] = "☐"

    def box_to_dash():
        for g in range(3):
            for f in range(3):
                if smol_board[g][f] == "☐":
                    smol_board[g][f] = "-"

    def no_colour_to_colour():
        for k in range(9):
            for l in range(3):
                for p in range(3):
                    if bigboard[k][l][p] == "X":
                        bigboard[k][l][p] = Fore.RED + "X" + Fore.WHITE
                    elif bigboard[k][l][p] == "O":
                        bigboard[k][l][p] = Fore.BLUE + "O" + Fore.WHITE
                    elif bigboard[k][l][p] == "-":
                        bigboard[k][l][p] = Fore.WHITE + "-" + Fore.WHITE
                    elif bigboard[k][l][p] == "☐":
                        bigboard[k][l][p] = Fore.WHITE + "☐" + Fore.WHITE             
        for y in range(9):
            if bigboard_values[y] == "X":
                bigboard_values[y] = Fore.RED + "X" + Fore.WHITE
                smol_box[y] = Fore.RED + "────┼─────┼────" + Fore.WHITE
            elif bigboard_values[y] == "O":
                bigboard_values[y] = Fore.BLUE + "O" + Fore.WHITE
                smol_box[y] = Fore.BLUE + "────┼─────┼────" + Fore.WHITE
            elif bigboard_values[y] == "Ø":
                bigboard_values[y] = Fore.GREEN + "Ø" + Fore.WHITE
                smol_box[y] = Fore.GREEN + "────┼─────┼────" + Fore.WHITE
            elif bigboard_values[y] == "-":
                bigboard_values[y] = Fore.WHITE + "-" + Fore.WHITE
                smol_box[y] = Fore.WHITE + "────┼─────┼────" + Fore.WHITE

    def colour_to_no_colour():
        for k in range(9):
            for l in range(3):
                for p in range(3):
                    if bigboard[k][l][p] == Fore.RED + "X" + Fore.WHITE:
                        bigboard[k][l][p] = "X"
                    elif bigboard[k][l][p] == Fore.BLUE + "O" + Fore.WHITE:
                        bigboard[k][l][p] = "O"
                    elif bigboard[k][l][p] == Fore.WHITE + "-" + Fore.WHITE:
                        bigboard[k][l][p] = "-"
                    elif bigboard[k][l][p] == Fore.WHITE + "☐" + Fore.WHITE:
                        bigboard[k][l][p] = "☐"                   
        for y in range(9):
            if bigboard_values[y] == Fore.RED + "X" + Fore.WHITE:
                bigboard_values[y] = "X"
            elif bigboard_values[y] == Fore.BLUE + "O" + Fore.WHITE:
                bigboard_values[y] = "O"
            elif bigboard_values[y] == Fore.GREEN + "Ø" + Fore.WHITE:
                bigboard_values[y] = "Ø"
            elif bigboard_values[y] == Fore.WHITE + "-" + Fore.WHITE:  
                bigboard_values[y] = "-"      

    #Win checking systems
    #Checking for a win on one of the small boards
    def smol_board_wincheck():
        global winvalue
        global EMPTY
        if bigboard_values[winvalue] == "-":
            if smol_board[0][0] == smol_board[1][0] == smol_board[2][0] != "-":
                if smol_board[0][0] == smol_board[1][0] == smol_board[2][0] == "X":
                    if bigboard_values[winvalue] != "O":
                        bigboard_values[winvalue] = "X"
                elif smol_board[0][0] == smol_board[1][0] == smol_board[2][0] == "O":
                    if bigboard_values[winvalue] != "X":
                        bigboard_values[winvalue] = "O"
            elif smol_board[0][1] == smol_board[1][1] == smol_board[2][1] != "-":
                if smol_board[0][1] == smol_board[1][1] == smol_board[2][1] == "X":
                    if bigboard_values[winvalue] != "O":
                        bigboard_values[winvalue] = "X"
                elif smol_board[0][1] == smol_board[1][1] == smol_board[2][1] == "O":
                    if bigboard_values[winvalue] != "X":
                        bigboard_values[winvalue] = "O"
            elif smol_board[0][2] == smol_board[1][2] == smol_board[2][2] != "-":
                if smol_board[0][2] == smol_board[1][2] == smol_board[2][2] == "X":
                    if bigboard_values[winvalue] != "O":
                        bigboard_values[winvalue] = "X"
                elif smol_board[0][2] == smol_board[1][2] == smol_board[2][2] == "O":
                    if bigboard_values[winvalue] != "X":
                        bigboard_values[winvalue] = "O"
            elif smol_board[0][0] == smol_board[0][1] == smol_board[0][2] != "-":
                if smol_board[0][0] == smol_board[0][1] == smol_board[0][2] == "X":
                    if bigboard_values[winvalue] != "O":
                        bigboard_values[winvalue] = "X"
                elif smol_board[0][0] == smol_board[0][1] == smol_board[0][2] == "O":
                    if bigboard_values[winvalue] != "X":
                        bigboard_values[winvalue] = "O"
            elif smol_board[1][0] == smol_board[1][1] == smol_board[1][2] != "-":
                if smol_board[1][0] == smol_board[1][1] == smol_board[1][2] == "X":
                    if bigboard_values[winvalue] != "O":
                        bigboard_values[winvalue] = "X"
                elif smol_board[1][0] == smol_board[1][1] == smol_board[1][2] == "O":
                    if bigboard_values[winvalue] != "X":
                        bigboard_values[winvalue] = "O"
            elif smol_board[2][0] == smol_board[2][1] == smol_board[2][2] != "-":
                if smol_board[2][0] == smol_board[2][1] == smol_board[2][2] == "X":
                    if bigboard_values[winvalue] != "O":
                        bigboard_values[winvalue] = "X"
                elif smol_board[2][0] == smol_board[2][1] == smol_board[2][2] == "O":
                    if bigboard_values[winvalue] != "X":
                        bigboard_values[winvalue] = "O"
            elif smol_board[0][0] == smol_board[1][1] == smol_board[2][2] != "-":
                if smol_board[0][0] == smol_board[1][1] == smol_board[2][2] == "X":
                    if bigboard_values[winvalue] != "O":
                        bigboard_values[winvalue] = "X"
                elif smol_board[0][0] == smol_board[1][1] == smol_board[2][2] == "O":
                    if bigboard_values[winvalue] != "X":
                        bigboard_values[winvalue] = "O"
            elif smol_board[2][0] == smol_board[1][1] == smol_board[0][2] != "-":
                if smol_board[2][0] == smol_board[1][1] == smol_board[0][2] == "X":            
                    bigboard_values[winvalue] = "X"
                elif smol_board[2][0] == smol_board[1][1] == smol_board[0][2] == "O":
                    if bigboard_values[winvalue] != "X":
                        bigboard_values[winvalue] = "O"
            elif "-" not in smol_board[0]:
                if "-" not in smol_board[1]:
                    if "-" not in smol_board[2]:
                        if bigboard_values == "O" or "X":
                            if bigboard_values[winvalue] == "-":
                                bigboard_values[winvalue] = "Ø"

    #Checking for a symbol that makes a win for both players, and checks if they have a win with such symbols for both players.
    def same_symbol():
        global same_winvalue
        global bigboard_values
        global row_check
        global loop_of_game
        global x
        global one_list
        global u
        global x_win
        global o_win
        global tie
        empty_list = []
        i = 0
        if "Ø" in bigboard_values:
            i = operator.countOf(bigboard_values, "Ø")
            for v in range(i):
                empty_list.append(bigboard_values.index("Ø"))
                bigboard_values[int(empty_list[v])] = "X"
            X_same_wincheck()
            for y in range(i):
                bigboard_values[int(empty_list[y])] = "O"
            O_same_wincheck()
            if row_check != 0:
                if same_winvalue > 0:
                    loop_of_game = False
                    x = Fore.RED + "│" + Fore.WHITE
                    one_list = Fore.RED + "────────────────────┼─────────────────────┼────────────────────" + Fore.WHITE
                    u = Fore.RED + "│ " + Fore.WHITE
                    user_friendly_print_bigboard_better()
                    print("")
                    print("X, you won!")
                elif same_winvalue < 0:
                    loop_of_game = False
                    x = Fore.BLUE + "│" + Fore.WHITE
                    one_list = Fore.BLUE + "────────────────────┼─────────────────────┼────────────────────" + Fore.WHITE
                    u = Fore.BLUE + "│ " + Fore.WHITE
                    user_friendly_print_bigboard_better()
                    print("")
                    print("O, you won!")
                elif same_winvalue == 0:
                    loop_of_game = False
                    x = Fore.GREEN + "│" + Fore.WHITE
                    one_list = Fore.GREEN + "────────────────────┼─────────────────────┼────────────────────" + Fore.WHITE
                    u = Fore.GREEN + "│ " + Fore.WHITE
                    user_friendly_print_bigboard_better()
                    print("")
                    print("It's a tie!")
            for z in range(i):
                bigboard_values[int(empty_list[z])] = "Ø"

    #Same symbol check, for the X player
    def X_same_wincheck():
        global same_winvalue
        global bigboard_values
        global row_check
        if bigboard_values[0] == bigboard_values[1] == bigboard_values[2] == "X" != "-":
            same_winvalue += 1
            row_check += 1
        if bigboard_values[3] == bigboard_values[4] == bigboard_values[5] == "X" != "-":
            same_winvalue += 1
            row_check += 1
        if bigboard_values[6] == bigboard_values[7] == bigboard_values[8] == "X" != "-":
            same_winvalue += 1
            row_check += 1
        if bigboard_values[0] == bigboard_values[3] == bigboard_values[6] == "X" != "-":
            same_winvalue += 1
            row_check += 1
        if bigboard_values[1] == bigboard_values[4] == bigboard_values[7] == "X" != "-":
            same_winvalue += 1
            row_check += 1
        if bigboard_values[2] == bigboard_values[5] == bigboard_values[8] == "X" != "-":
            same_winvalue += 1
            row_check += 1
        if bigboard_values[0] == bigboard_values[4] == bigboard_values[8] == "X" != "-":
            same_winvalue += 1
            row_check += 1
        if bigboard_values[2] == bigboard_values[4] == bigboard_values[6] == "X" != "-":
            same_winvalue += 1
            row_check += 1

    #Same symbol check, for the O player
    def O_same_wincheck():
        global same_winvalue
        global bigboard_values
        global row_check
        if bigboard_values[0] == bigboard_values[1] == bigboard_values[2] == "O" != "-":
            same_winvalue = same_winvalue - 1
            row_check += 1
        if bigboard_values[3] == bigboard_values[4] == bigboard_values[5] == "O" != "-":
            same_winvalue = same_winvalue - 1
            row_check += 1
        if bigboard_values[6] == bigboard_values[7] == bigboard_values[8] == "O" != "-":
            same_winvalue = same_winvalue - 1
            row_check += 1
        if bigboard_values[0] == bigboard_values[3] == bigboard_values[6] == "O" != "-":
            same_winvalue = same_winvalue - 1
            row_check += 1
        if bigboard_values[1] == bigboard_values[4] == bigboard_values[7] == "O" != "-":
            same_winvalue = same_winvalue - 1
            row_check += 1
        if bigboard_values[2] == bigboard_values[5] == bigboard_values[8] == "O" != "-":
            same_winvalue = same_winvalue - 1
            row_check += 1
        if bigboard_values[0] == bigboard_values[4] == bigboard_values[8] == "O" != "-":
            same_winvalue = same_winvalue - 1
            row_check += 1
        if bigboard_values[2] == bigboard_values[4] == bigboard_values[6] == "O" != "-":
            same_winvalue = same_winvalue - 1
            row_check += 1

    #Checks for a win on the bigboard
    def bigboard_board_wincheck():
        global loop_of_game
        global x
        global one_list
        global u
        if bigboard_values[0] == bigboard_values[1] == bigboard_values[2] != "-":
            if loop_of_game is True:       
                loop_of_game = False
                if bigboard_values[0] == "X":
                    x = Fore.RED + "│" + Fore.WHITE
                    one_list = Fore.RED + "────────────────────┼─────────────────────┼────────────────────" + Fore.WHITE
                    u = Fore.RED + "│ " + Fore.WHITE
                elif bigboard_values[0] == "O":
                    x = Fore.BLUE + "│" + Fore.WHITE
                    one_list = Fore.BLUE + "────────────────────┼─────────────────────┼────────────────────" + Fore.WHITE
                    u = Fore.BLUE + "│ " + Fore.WHITE
                user_friendly_print_bigboard_better()
                print("")
                print(bigboard_values[0] + ", you won!")
        elif bigboard_values[3] == bigboard_values[4] == bigboard_values[5] != "-":
            if loop_of_game is True:
                loop_of_game = False
                if bigboard_values[3] == "X":
                    x = Fore.RED + "│" + Fore.WHITE
                    one_list = Fore.RED + "────────────────────┼─────────────────────┼────────────────────" + Fore.WHITE
                    u = Fore.RED + "│ " + Fore.WHITE
                elif bigboard_values[3] == "O":
                    x = Fore.BLUE + "│" + Fore.WHITE
                    one_list = Fore.BLUE + "────────────────────┼─────────────────────┼────────────────────" + Fore.WHITE
                    u = Fore.BLUE + "│ " + Fore.WHITE
                user_friendly_print_bigboard_better()
                print("")
                print(bigboard_values[3] + ", you won!")
        elif bigboard_values[6] == bigboard_values[7] == bigboard_values[8] != "-":
            if loop_of_game is True:
                loop_of_game = False
                if bigboard_values[6] == "X":
                    x = Fore.RED + "│" + Fore.WHITE
                    one_list = Fore.RED + "────────────────────┼─────────────────────┼────────────────────" + Fore.WHITE
                    u = Fore.RED + "│ " + Fore.WHITE
                elif bigboard_values[6] == "O":
                    x = Fore.BLUE + "│" + Fore.WHITE
                    one_list = Fore.BLUE + "────────────────────┼─────────────────────┼────────────────────" + Fore.WHITE
                    u = Fore.BLUE + "│ " + Fore.WHITE
                user_friendly_print_bigboard_better()
                print("")
                print(bigboard_values[6] + ", you won!")
        elif bigboard_values[0] == bigboard_values[4] == bigboard_values[8] != "-":
            if loop_of_game is True:
                loop_of_game = False
                if bigboard_values[0] == "X":
                    x = Fore.RED + "│" + Fore.WHITE
                    one_list = Fore.RED + "────────────────────┼─────────────────────┼────────────────────" + Fore.WHITE
                    u = Fore.RED + "│ " + Fore.WHITE
                elif bigboard_values[0] == "O":
                    x = Fore.BLUE + "│" + Fore.WHITE
                    one_list = Fore.BLUE + "────────────────────┼─────────────────────┼────────────────────" + Fore.WHITE
                    u = Fore.BLUE + "│ " + Fore.WHITE
                user_friendly_print_bigboard_better()
                print("")
                print(bigboard_values[0] + ", you won!")
        elif bigboard_values[2] == bigboard_values[4] == bigboard_values[6] != "-":
            if loop_of_game is True:
                loop_of_game = False
                if bigboard_values[2] == "X":
                    x = Fore.RED + "│" + Fore.WHITE
                    one_list = Fore.RED + "────────────────────┼─────────────────────┼────────────────────" + Fore.WHITE
                    u = Fore.RED + "│ " + Fore.WHITE
                elif bigboard_values[2] == "O":
                    x = Fore.BLUE + "│" + Fore.WHITE
                    one_list = Fore.BLUE + "────────────────────┼─────────────────────┼────────────────────" + Fore.WHITE
                    u = Fore.BLUE + "│ " + Fore.WHITE
                user_friendly_print_bigboard_better()
                print("")
                print(bigboard_values[2] + ", you won!")
        elif bigboard_values[0] == bigboard_values[3] == bigboard_values[6] != "-":
            if loop_of_game is True:
                loop_of_game = False
                if bigboard_values[0] == "X":
                    x = Fore.RED + "│" + Fore.WHITE
                    one_list = Fore.RED + "────────────────────┼─────────────────────┼────────────────────" + Fore.WHITE
                    u = Fore.RED + "│ " + Fore.WHITE
                elif bigboard_values[0] == "O":
                    x = Fore.BLUE + "│" + Fore.WHITE
                    one_list = Fore.BLUE + "────────────────────┼─────────────────────┼────────────────────" + Fore.WHITE
                    u = Fore.BLUE + "│ " + Fore.WHITE
                user_friendly_print_bigboard_better()
                print("")
                print(bigboard_values[0] + ", you won!")
        elif bigboard_values[1] == bigboard_values[4] == bigboard_values[7] != "-":
            if loop_of_game is True:
                loop_of_game = False
                if bigboard_values[1] == "X":
                    x = Fore.RED + "│" + Fore.WHITE
                    one_list = Fore.RED + "────────────────────┼─────────────────────┼────────────────────" + Fore.WHITE
                    u = Fore.RED + "│ " + Fore.WHITE
                elif bigboard_values[1] == "O":
                    x = Fore.BLUE + "│" + Fore.WHITE
                    one_list = Fore.BLUE + "────────────────────┼─────────────────────┼────────────────────" + Fore.WHITE
                    u = Fore.BLUE + "│ " + Fore.WHITE
                user_friendly_print_bigboard_better()
                print("")
                print(bigboard_values[1] + ", you won!")
        elif bigboard_values[2] == bigboard_values[5] == bigboard_values[8] != "-":
            if loop_of_game is True:
                loop_of_game = False
                if bigboard_values[2] == "X":
                    x = Fore.RED + "│" + Fore.WHITE
                    one_list = Fore.RED + "────────────────────┼─────────────────────┼────────────────────" + Fore.WHITE
                    u = Fore.RED + "│ " + Fore.WHITE
                elif bigboard_values[2] == "O":
                    x = Fore.BLUE + "│" + Fore.WHITE
                    one_list = Fore.BLUE + "────────────────────┼─────────────────────┼────────────────────" + Fore.WHITE
                    u = Fore.BLUE + "│ " + Fore.WHITE
                user_friendly_print_bigboard_better()
                print("")
                print(bigboard_values[2] + ", you won!")    
        elif loop_of_game is True:
            same_symbol()
        elif "-" not in bigboard_values:
            if loop_of_game is True:
                loop_of_game = False
                x = Fore.GREEN + "│" + Fore.WHITE
                one_list = Fore.GREEN + "────────────────────┼─────────────────────┼────────────────────" + Fore.WHITE
                u = Fore.GREEN + "│ " + Fore.WHITE
                user_friendly_print_bigboard_better()
                print("")
                print("It's a tie!")
            
    #board functions
    #Checks if a board is full with a win 
    def full_board_with_win():
        global full_board
        global user_friendly_variable
        global smol_board
        if loop_of_game is True:
            if "-" not in fullvalue[0]:
                if "-" not in fullvalue[1]:
                    if "-" not in fullvalue[2]:
                        while full_board == 1:
                            clear()
                            manual_print_bigboard()
                            new_board = input("Oh no! The board that has been chosen is full. Choose a new board: ")
                            if len(new_board) == 1:
                                if new_board in "123456789":
                                    new_board = int(new_board) - 1
                                    if 0 <= new_board < 10:
                                        smol_board_check = bigboard[new_board]
                                        if "-" not in smol_board_check[0]:
                                            if "-" not in smol_board_check[1]:
                                                if "-" not in smol_board_check[2]:
                                                    pass
                                                elif "-" in smol_board_check[2]:
                                                    full_board += 1
                                                    smol_board = smol_board_check
                                                    full_value = smol_board
                                                    user_friendly_variable = new_board
                                                    clear()
                                                    print_board_neatly()
                                                    user_friendly_print_bigboard_better()
                                                else:
                                                    print("How did you get here? How. There is either a hyphen or not in a board. What did you do. Please discuss this with me if you have found this message becasue you are really not supposed to find this.")
                                            elif "-" in smol_board_check[1]:
                                                full_board += 1
                                                smol_board = smol_board_check
                                                full_value = smol_board
                                                user_friendly_variable = new_board
                                                clear()
                                                print_board_neatly()
                                                user_friendly_print_bigboard_better()
                                            else:
                                                print("How did you get here? How. There is either a hyphen or not in a board. What did you do. Please discuss this with me if you have found this message becasue you are really not supposed to find this.")
                                        elif "-" in smol_board_check[0]:
                                            full_board += 1
                                            smol_board = smol_board_check
                                            full_value = smol_board
                                            user_friendly_variable = new_board
                                            clear()
                                            print_board_neatly()
                                            user_friendly_print_bigboard_better()
                                        else: 
                                            print("How did you get here? How. There is either a hyphen or not in a board. What did you do. Please discuss this with me if you have found this message becasue you are really not supposed to find this.")

    #Ai board functions
    #Removes the full board from random ai choices
    def full_board_ai_removal():
        global list_of_full
        for x in range(9):
            if "-" not in bigboard[x][0]:
                if "-" not in bigboard[x][1]:
                    if "-" not in bigboard[x][2]:
                        if x == 0:
                            if 0 in list_of_full:
                                list_of_full.remove(0)
                        elif x == 1:
                            if 1 in list_of_full:
                                list_of_full.remove(1)
                        elif x == 2:
                            if 2 in list_of_full:
                                list_of_full.remove(2)
                        elif x == 3:
                            if 3 in list_of_full:
                                list_of_full.remove(3)
                        elif x == 4:
                            if 4 in list_of_full:
                                list_of_full.remove(4)
                        elif x == 5:
                            if 5 in list_of_full:
                                list_of_full.remove(5)
                        elif x == 6:
                            if 6 in list_of_full:
                                list_of_full.remove(6)
                        elif x == 7:
                            if 7 in list_of_full:
                                list_of_full.remove(7)
                        elif x == 8:
                            if 8 in list_of_full:
                                list_of_full.remove(8)
                        else:
                            smol_board_wincheck()
                            bigboard_board_wincheck()

    #Checks if a board is full
    def full_board_with_win_ai():
        global full_board
        global user_friendly_variable
        global smol_board
        global list_of_full
        global fullvalue
        if loop_of_game is True:
            if "-" not in fullvalue[0]:
                if "-" not in fullvalue[1]:
                    if "-" not in fullvalue[2]:
                        full_board_ai_removal()
                        if len(list_of_full) != 0:
                            new_board = bigboard[int(random.choice(list_of_full))]
                            smol_board_check = new_board
                            full_board += 1
                            smol_board = smol_board_check
                            full_value = smol_board
                            user_friendly_variable = new_board
                            print_board_neatly()
                        else:
                            smol_board_wincheck()
                            bigboard_board_wincheck()

    #Print board functions
    #Creates the main lines to use to print a better bigboard
    def print_board_neatly():
        global better_board
        global Ø_colour
        global X_colour
        global O_colour
        global dash_colour
        better_board = []
        for y in range(9):
            for x in range(3):
                temp_string = (Fore.WHITE + bigboard[y][x][0], bigboard[y][x][1], bigboard[y][x][2] + Fore.WHITE)
                if bigboard_values[y] == Fore.WHITE + "-" + Fore.WHITE:
                    temp_string2 = dash_colour.join(temp_string) + Fore.WHITE  
                    better_board.append(Fore.WHITE + temp_string2 + Fore.WHITE)
                elif bigboard_values[y] == Fore.RED + "X" + Fore.WHITE:
                    temp_string2 = X_colour.join(temp_string) + Fore.WHITE  
                    better_board.append(Fore.WHITE + temp_string2 + Fore.WHITE)
                elif bigboard_values[y] == Fore.BLUE + "O" + Fore.WHITE:
                    temp_string2 = O_colour.join(temp_string) + Fore.WHITE  
                    better_board.append(Fore.WHITE + temp_string2 + Fore.WHITE)
                elif bigboard_values[y] == Fore.GREEN + "Ø" + Fore.WHITE:
                    temp_string2 = Ø_colour.join(temp_string) + Fore.WHITE  
                    better_board.append(Fore.WHITE + temp_string2 + Fore.WHITE)

    #Prints the bigboard with values and lines
    def user_friendly_print_bigboard_better():
        global x 
        global user_friendly_variable
        global one_list
        global u
        dash_to_box()
        no_colour_to_colour()
        print_board_neatly()
        print(Fore.WHITE)
        if user_friendly_variable == 0:
            print(N*3, "1", N*3, "2", N*3, "3")
            print(Fore.WHITE + "a", N, better_board[0] + Fore.WHITE, "   " , x , N, better_board[3] + Fore.WHITE, "   " , x , N, better_board[6] + Fore.WHITE)
            print(N*2 , smol_box[0], N*2, u, smol_box[1], N*2, u, smol_box[2])
            print(Fore.WHITE + "b", N, better_board[1] + Fore.WHITE, " ", bigboard_values[0] + Fore.WHITE, x , N, better_board[4] + Fore.WHITE, " ", bigboard_values[1] + Fore.WHITE, x , N,  better_board[7], " ", bigboard_values[2] + Fore.WHITE)
            print(N*2 , smol_box[0], N*2, u, smol_box[1], N*2, u, smol_box[2])
            print(Fore.WHITE + "c", N, better_board[2] + Fore.WHITE, "   " , x , N, better_board[5] + Fore.WHITE, "   " , x , N, better_board[8] + Fore.WHITE)
            print(Fore.WHITE + N, one_list)
            print(Fore.WHITE + N, N, better_board[9] + Fore.WHITE, "   " , x , N, better_board[12] + Fore.WHITE, "   " , x , N, better_board[15] + Fore.WHITE)
            print(N*2 , smol_box[3], N*2, u, smol_box[4], N*2, u, smol_box[5])
            print(Fore.WHITE + N, N, better_board[10] + Fore.WHITE, " ", bigboard_values[3] + Fore.WHITE, x , N, better_board[13] + Fore.WHITE, " ", bigboard_values[4] + Fore.WHITE, x , N, better_board[16], " ", bigboard_values[5] + Fore.WHITE) 
            print(N*2 , smol_box[3], N*2, u, smol_box[4], N*2, u, smol_box[5])
            print(Fore.WHITE + N, N, better_board[11] + Fore.WHITE, "   " , x , N, better_board[14] + Fore.WHITE, "   " , x , N, better_board[17] + Fore.WHITE)
            print(Fore.WHITE + N, one_list)
            print(Fore.WHITE + N, N, better_board[18] + Fore.WHITE, "   " , x , N, better_board[21] + Fore.WHITE, "   " , x , N, better_board[24] + Fore.WHITE)
            print(N*2 , smol_box[6], N*2, u, smol_box[7], N*2, u, smol_box[8])
            print(Fore.WHITE + N, N, better_board[19] + Fore.WHITE, " ", bigboard_values[6] + Fore.WHITE, x , N, better_board[22] + Fore.WHITE, " ", bigboard_values[7] + Fore.WHITE, x , N, better_board[25] + Fore.WHITE, " ", bigboard_values[8] + Fore.WHITE)
            print(N*2 , smol_box[6], N*2, u, smol_box[7], N*2, u, smol_box[8])
            print(Fore.WHITE + N, N, better_board[20] + Fore.WHITE, "   " , x , N, better_board[23] + Fore.WHITE, "   " , x , N, better_board[26] + Fore.WHITE)
            box_to_dash()
            colour_to_no_colour()
        elif user_friendly_variable == 1:
            print(N*25, "1", N*3, "2", N*3, "3")
            print(Fore.WHITE + "a", N, better_board[0] + Fore.WHITE, "   " , x , N, better_board[3] + Fore.WHITE, "   " , x , N, better_board[6] + Fore.WHITE)
            print(N*2 , smol_box[0], N*2, u, smol_box[1], N*2, u, smol_box[2])
            print(Fore.WHITE + "b", N, better_board[1] + Fore.WHITE, " ", bigboard_values[0] + Fore.WHITE, x , N, better_board[4] + Fore.WHITE, " ", bigboard_values[1] + Fore.WHITE, x , N,  better_board[7], " ", bigboard_values[2] + Fore.WHITE)
            print(N*2 , smol_box[0], N*2, u, smol_box[1], N*2, u, smol_box[2])
            print(Fore.WHITE + "c", N, better_board[2] + Fore.WHITE, "   " , x , N, better_board[5] + Fore.WHITE, "   " , x , N, better_board[8] + Fore.WHITE)
            print(Fore.WHITE + N, one_list)
            print(Fore.WHITE + N, N, better_board[9] + Fore.WHITE, "   " , x , N, better_board[12] + Fore.WHITE, "   " , x , N, better_board[15] + Fore.WHITE)
            print(N*2 , smol_box[3], N*2, u, smol_box[4], N*2, u, smol_box[5])
            print(Fore.WHITE + N, N, better_board[10] + Fore.WHITE, " ", bigboard_values[3] + Fore.WHITE, x , N, better_board[13] + Fore.WHITE, " ", bigboard_values[4] + Fore.WHITE, x , N, better_board[16], " ", bigboard_values[5] + Fore.WHITE) 
            print(N*2 , smol_box[3], N*2, u, smol_box[4], N*2, u, smol_box[5])
            print(Fore.WHITE + N, N, better_board[11] + Fore.WHITE, "   " , x , N, better_board[14] + Fore.WHITE, "   " , x , N, better_board[17] + Fore.WHITE)
            print(Fore.WHITE + N, one_list)
            print(Fore.WHITE + N, N, better_board[18] + Fore.WHITE, "   " , x , N, better_board[21] + Fore.WHITE, "   " , x , N, better_board[24] + Fore.WHITE)
            print(N*2 , smol_box[6], N*2, u, smol_box[7], N*2, u, smol_box[8])
            print(Fore.WHITE + N, N, better_board[19] + Fore.WHITE, " ", bigboard_values[6] + Fore.WHITE, x , N, better_board[22] + Fore.WHITE, " ", bigboard_values[7] + Fore.WHITE, x , N, better_board[25] + Fore.WHITE, " ", bigboard_values[8] + Fore.WHITE)
            print(N*2 , smol_box[6], N*2, u, smol_box[7], N*2, u, smol_box[8])
            print(Fore.WHITE + N, N, better_board[20] + Fore.WHITE, "   " , x , N, better_board[23] + Fore.WHITE, "   " , x , N, better_board[26] + Fore.WHITE)
            box_to_dash()
            colour_to_no_colour()
        elif user_friendly_variable == 2:
            print(N*47, "1", N*3, "2", N*3, "3")
            print(Fore.WHITE + "a", N, better_board[0] + Fore.WHITE, "   " , x , N, better_board[3] + Fore.WHITE, "   " , x , N, better_board[6] + Fore.WHITE)
            print(N*2 , smol_box[0], N*2, u, smol_box[1], N*2, u, smol_box[2])
            print(Fore.WHITE + "b", N, better_board[1] + Fore.WHITE, " ", bigboard_values[0] + Fore.WHITE, x , N, better_board[4] + Fore.WHITE, " ", bigboard_values[1] + Fore.WHITE, x , N,  better_board[7], " ", bigboard_values[2] + Fore.WHITE)
            print(N*2 , smol_box[0], N*2, u, smol_box[1], N*2, u, smol_box[2])
            print(Fore.WHITE + "c", N, better_board[2] + Fore.WHITE, "   " , x , N, better_board[5] + Fore.WHITE, "   " , x , N, better_board[8] + Fore.WHITE)
            print(Fore.WHITE + N, one_list)
            print(Fore.WHITE + N, N, better_board[9] + Fore.WHITE, "   " , x , N, better_board[12] + Fore.WHITE, "   " , x , N, better_board[15] + Fore.WHITE)
            print(N*2 , smol_box[3], N*2, u, smol_box[4], N*2, u, smol_box[5])
            print(Fore.WHITE + N, N, better_board[10] + Fore.WHITE, " ", bigboard_values[3] + Fore.WHITE, x , N, better_board[13] + Fore.WHITE, " ", bigboard_values[4] + Fore.WHITE, x , N, better_board[16], " ", bigboard_values[5] + Fore.WHITE) 
            print(N*2 , smol_box[3], N*2, u, smol_box[4], N*2, u, smol_box[5])
            print(Fore.WHITE + N, N, better_board[11] + Fore.WHITE, "   " , x , N, better_board[14] + Fore.WHITE, "   " , x , N, better_board[17] + Fore.WHITE)
            print(Fore.WHITE + N, one_list)
            print(Fore.WHITE + N, N, better_board[18] + Fore.WHITE, "   " , x , N, better_board[21] + Fore.WHITE, "   " , x , N, better_board[24] + Fore.WHITE)
            print(N*2 , smol_box[6], N*2, u, smol_box[7], N*2, u, smol_box[8])
            print(Fore.WHITE + N, N, better_board[19] + Fore.WHITE, " ", bigboard_values[6] + Fore.WHITE, x , N, better_board[22] + Fore.WHITE, " ", bigboard_values[7] + Fore.WHITE, x , N, better_board[25] + Fore.WHITE, " ", bigboard_values[8] + Fore.WHITE)
            print(N*2 , smol_box[6], N*2, u, smol_box[7], N*2, u, smol_box[8])
            print(Fore.WHITE + N, N, better_board[20] + Fore.WHITE, "   " , x , N, better_board[23] + Fore.WHITE, "   " , x , N, better_board[26] + Fore.WHITE)
            box_to_dash()
            colour_to_no_colour()
        elif user_friendly_variable == 3:
            print(N*3, "1", N*3, "2", N*3, "3")
            print(Fore.WHITE + N, N, better_board[0] + Fore.WHITE, "   " , x , N, better_board[3] + Fore.WHITE, "   " , x , N, better_board[6] + Fore.WHITE)
            print(N*2 , smol_box[0], N*2, u, smol_box[1], N*2, u, smol_box[2])
            print(Fore.WHITE + N, N, better_board[1] + Fore.WHITE, " ", bigboard_values[0] + Fore.WHITE, x , N, better_board[4] + Fore.WHITE, " ", bigboard_values[1] + Fore.WHITE, x , N,  better_board[7], " ", bigboard_values[2] + Fore.WHITE)
            print(N*2 , smol_box[0], N*2, u, smol_box[1], N*2, u, smol_box[2])
            print(Fore.WHITE + N, N, better_board[2] + Fore.WHITE, "   " , x , N, better_board[5] + Fore.WHITE, "   " , x , N, better_board[8] + Fore.WHITE)
            print(Fore.WHITE + N, one_list)
            print(Fore.WHITE + "a", N, better_board[9] + Fore.WHITE, "   " , x , N, better_board[12] + Fore.WHITE, "   " , x , N, better_board[15] + Fore.WHITE)
            print(N*2 , smol_box[3], N*2, u, smol_box[4], N*2, u, smol_box[5])
            print(Fore.WHITE + "b", N, better_board[10] + Fore.WHITE, " ", bigboard_values[3] + Fore.WHITE, x , N, better_board[13] + Fore.WHITE, " ", bigboard_values[4] + Fore.WHITE, x , N, better_board[16], " ", bigboard_values[5] + Fore.WHITE) 
            print(N*2 , smol_box[3], N*2, u, smol_box[4], N*2, u, smol_box[5])
            print(Fore.WHITE + "c", N, better_board[11] + Fore.WHITE, "   " , x , N, better_board[14] + Fore.WHITE, "   " , x , N, better_board[17] + Fore.WHITE)
            print(Fore.WHITE + N, one_list)
            print(Fore.WHITE + N, N, better_board[18] + Fore.WHITE, "   " , x , N, better_board[21] + Fore.WHITE, "   " , x , N, better_board[24] + Fore.WHITE)
            print(N*2 , smol_box[6], N*2, u, smol_box[7], N*2, u, smol_box[8])
            print(Fore.WHITE + N, N, better_board[19] + Fore.WHITE, " ", bigboard_values[6] + Fore.WHITE, x , N, better_board[22] + Fore.WHITE, " ", bigboard_values[7] + Fore.WHITE, x , N, better_board[25] + Fore.WHITE, " ", bigboard_values[8] + Fore.WHITE)
            print(N*2 , smol_box[6], N*2, u, smol_box[7], N*2, u, smol_box[8])
            print(Fore.WHITE + N, N, better_board[20] + Fore.WHITE, "   " , x , N, better_board[23] + Fore.WHITE, "   " , x , N, better_board[26] + Fore.WHITE)
            box_to_dash()
            colour_to_no_colour()
        elif user_friendly_variable == 4:
            print(N*25, "1", N*3, "2", N*3, "3")
            print(Fore.WHITE + N, N, better_board[0] + Fore.WHITE, "   " , x , N, better_board[3] + Fore.WHITE, "   " , x , N, better_board[6] + Fore.WHITE)
            print(N*2 , smol_box[0], N*2, u, smol_box[1], N*2, u, smol_box[2])
            print(Fore.WHITE + N, N, better_board[1] + Fore.WHITE, " ", bigboard_values[0] + Fore.WHITE, x , N, better_board[4] + Fore.WHITE, " ", bigboard_values[1] + Fore.WHITE, x , N,  better_board[7], " ", bigboard_values[2] + Fore.WHITE)
            print(N*2 , smol_box[0], N*2, u, smol_box[1], N*2, u, smol_box[2])
            print(Fore.WHITE + N, N, better_board[2] + Fore.WHITE, "   " , x , N, better_board[5] + Fore.WHITE, "   " , x , N, better_board[8] + Fore.WHITE)
            print(Fore.WHITE + N, one_list)
            print(Fore.WHITE + "a", N, better_board[9] + Fore.WHITE, "   " , x , N, better_board[12] + Fore.WHITE, "   " , x , N, better_board[15] + Fore.WHITE)
            print(N*2 , smol_box[3], N*2, u, smol_box[4], N*2, u, smol_box[5])
            print(Fore.WHITE + "b", N, better_board[10] + Fore.WHITE, " ", bigboard_values[3] + Fore.WHITE, x , N, better_board[13] + Fore.WHITE, " ", bigboard_values[4] + Fore.WHITE, x , N, better_board[16], " ", bigboard_values[5] + Fore.WHITE) 
            print(N*2 , smol_box[3], N*2, u, smol_box[4], N*2, u, smol_box[5])
            print(Fore.WHITE + "c", N, better_board[11] + Fore.WHITE, "   " , x , N, better_board[14] + Fore.WHITE, "   " , x , N, better_board[17] + Fore.WHITE)
            print(Fore.WHITE + N, one_list)
            print(Fore.WHITE + N, N, better_board[18] + Fore.WHITE, "   " , x , N, better_board[21] + Fore.WHITE, "   " , x , N, better_board[24] + Fore.WHITE)
            print(N*2 , smol_box[6], N*2, u, smol_box[7], N*2, u, smol_box[8])
            print(Fore.WHITE + N, N, better_board[19] + Fore.WHITE, " ", bigboard_values[6] + Fore.WHITE, x , N, better_board[22] + Fore.WHITE, " ", bigboard_values[7] + Fore.WHITE, x , N, better_board[25] + Fore.WHITE, " ", bigboard_values[8] + Fore.WHITE)
            print(N*2 , smol_box[6], N*2, u, smol_box[7], N*2, u, smol_box[8])
            print(Fore.WHITE + N, N, better_board[20] + Fore.WHITE, "   " , x , N, better_board[23] + Fore.WHITE, "   " , x , N, better_board[26] + Fore.WHITE)
            box_to_dash()
            colour_to_no_colour()
        elif user_friendly_variable == 5:
            print(N*47, "1", N*3, "2", N*3, "3")
            print(Fore.WHITE + N, N, better_board[0] + Fore.WHITE, "   " , x , N, better_board[3] + Fore.WHITE, "   " , x , N, better_board[6] + Fore.WHITE)
            print(N*2 , smol_box[0], N*2, u, smol_box[1], N*2, u, smol_box[2])
            print(Fore.WHITE + N, N, better_board[1] + Fore.WHITE, " ", bigboard_values[0] + Fore.WHITE, x , N, better_board[4] + Fore.WHITE, " ", bigboard_values[1] + Fore.WHITE, x , N,  better_board[7], " ", bigboard_values[2] + Fore.WHITE)
            print(N*2 , smol_box[0], N*2, u, smol_box[1], N*2, u, smol_box[2])
            print(Fore.WHITE + N, N, better_board[2] + Fore.WHITE, "   " , x , N, better_board[5] + Fore.WHITE, "   " , x , N, better_board[8] + Fore.WHITE)
            print(Fore.WHITE + N, one_list)
            print(Fore.WHITE + "a", N, better_board[9] + Fore.WHITE, "   " , x , N, better_board[12] + Fore.WHITE, "   " , x , N, better_board[15] + Fore.WHITE)
            print(N*2 , smol_box[3], N*2, u, smol_box[4], N*2, u, smol_box[5])
            print(Fore.WHITE + "b", N, better_board[10] + Fore.WHITE, " ", bigboard_values[3] + Fore.WHITE, x , N, better_board[13] + Fore.WHITE, " ", bigboard_values[4] + Fore.WHITE, x , N, better_board[16], " ", bigboard_values[5] + Fore.WHITE) 
            print(N*2 , smol_box[3], N*2, u, smol_box[4], N*2, u, smol_box[5])
            print(Fore.WHITE + "c", N, better_board[11] + Fore.WHITE, "   " , x , N, better_board[14] + Fore.WHITE, "   " , x , N, better_board[17] + Fore.WHITE)
            print(Fore.WHITE + N, one_list)
            print(Fore.WHITE + N, N, better_board[18] + Fore.WHITE, "   " , x , N, better_board[21] + Fore.WHITE, "   " , x , N, better_board[24] + Fore.WHITE)
            print(N*2 , smol_box[6], N*2, u, smol_box[7], N*2, u, smol_box[8])
            print(Fore.WHITE + N, N, better_board[19] + Fore.WHITE, " ", bigboard_values[6] + Fore.WHITE, x , N, better_board[22] + Fore.WHITE, " ", bigboard_values[7] + Fore.WHITE, x , N, better_board[25] + Fore.WHITE, " ", bigboard_values[8] + Fore.WHITE)
            print(N*2 , smol_box[6], N*2, u, smol_box[7], N*2, u, smol_box[8])
            print(Fore.WHITE + N, N, better_board[20] + Fore.WHITE, "   " , x , N, better_board[23] + Fore.WHITE, "   " , x , N, better_board[26] + Fore.WHITE)
            box_to_dash()
            colour_to_no_colour()
        elif user_friendly_variable == 6:
            print(N*3, "1", N*3, "2", N*3, "3")
            print(Fore.WHITE + N, N, better_board[0] + Fore.WHITE, "   " , x , N, better_board[3] + Fore.WHITE, "   " , x , N, better_board[6] + Fore.WHITE)
            print(N*2 , smol_box[0], N*2, u, smol_box[1], N*2, u, smol_box[2])
            print(Fore.WHITE + N, N, better_board[1] + Fore.WHITE, " ", bigboard_values[0] + Fore.WHITE, x , N, better_board[4] + Fore.WHITE, " ", bigboard_values[1] + Fore.WHITE, x , N,  better_board[7], " ", bigboard_values[2] + Fore.WHITE)
            print(N*2 , smol_box[0], N*2, u, smol_box[1], N*2, u, smol_box[2])
            print(Fore.WHITE + N, N, better_board[2] + Fore.WHITE, "   " , x , N, better_board[5] + Fore.WHITE, "   " , x , N, better_board[8] + Fore.WHITE)
            print(Fore.WHITE + N, one_list)
            print(Fore.WHITE + N, N, better_board[9] + Fore.WHITE, "   " , x , N, better_board[12] + Fore.WHITE, "   " , x , N, better_board[15] + Fore.WHITE)
            print(N*2 , smol_box[3], N*2, u, smol_box[4], N*2, u, smol_box[5])
            print(Fore.WHITE + N, N, better_board[10] + Fore.WHITE, " ", bigboard_values[3] + Fore.WHITE, x , N, better_board[13] + Fore.WHITE, " ", bigboard_values[4] + Fore.WHITE, x , N, better_board[16], " ", bigboard_values[5] + Fore.WHITE) 
            print(N*2 , smol_box[3], N*2, u, smol_box[4], N*2, u, smol_box[5])
            print(Fore.WHITE + N, N, better_board[11] + Fore.WHITE, "   " , x , N, better_board[14] + Fore.WHITE, "   " , x , N, better_board[17] + Fore.WHITE)
            print(Fore.WHITE + N, one_list)
            print(Fore.WHITE + "a", N, better_board[18] + Fore.WHITE, "   " , x , N, better_board[21] + Fore.WHITE, "   " , x , N, better_board[24] + Fore.WHITE)
            print(N*2 , smol_box[6], N*2, u, smol_box[7], N*2, u, smol_box[8])
            print(Fore.WHITE + "b", N, better_board[19] + Fore.WHITE, " ", bigboard_values[6] + Fore.WHITE, x , N, better_board[22] + Fore.WHITE, " ", bigboard_values[7] + Fore.WHITE, x , N, better_board[25] + Fore.WHITE, " ", bigboard_values[8] + Fore.WHITE)
            print(N*2 , smol_box[6], N*2, u, smol_box[7], N*2, u, smol_box[8])
            print(Fore.WHITE + "c", N, better_board[20] + Fore.WHITE, "   " , x , N, better_board[23] + Fore.WHITE, "   " , x , N, better_board[26] + Fore.WHITE)
            box_to_dash()
            colour_to_no_colour()
        elif user_friendly_variable == 7:
            print(N*25, "1", N*3, "2", N*3, "3")
            print(Fore.WHITE + N, N, better_board[0] + Fore.WHITE, "   " , x , N, better_board[3] + Fore.WHITE, "   " , x , N, better_board[6] + Fore.WHITE)
            print(N*2 , smol_box[0], N*2, u, smol_box[1], N*2, u, smol_box[2])
            print(Fore.WHITE + N, N, better_board[1] + Fore.WHITE, " ", bigboard_values[0] + Fore.WHITE, x , N, better_board[4] + Fore.WHITE, " ", bigboard_values[1] + Fore.WHITE, x , N,  better_board[7], " ", bigboard_values[2] + Fore.WHITE)
            print(N*2 , smol_box[0], N*2, u, smol_box[1], N*2, u, smol_box[2])
            print(Fore.WHITE + N, N, better_board[2] + Fore.WHITE, "   " , x , N, better_board[5] + Fore.WHITE, "   " , x , N, better_board[8] + Fore.WHITE)
            print(Fore.WHITE + N, one_list)
            print(Fore.WHITE + N, N, better_board[9] + Fore.WHITE, "   " , x , N, better_board[12] + Fore.WHITE, "   " , x , N, better_board[15] + Fore.WHITE)
            print(N*2 , smol_box[3], N*2, u, smol_box[4], N*2, u, smol_box[5])
            print(Fore.WHITE + N, N, better_board[10] + Fore.WHITE, " ", bigboard_values[3] + Fore.WHITE, x , N, better_board[13] + Fore.WHITE, " ", bigboard_values[4] + Fore.WHITE, x , N, better_board[16], " ", bigboard_values[5] + Fore.WHITE) 
            print(N*2 , smol_box[3], N*2, u, smol_box[4], N*2, u, smol_box[5])
            print(Fore.WHITE + N, N, better_board[11] + Fore.WHITE, "   " , x , N, better_board[14] + Fore.WHITE, "   " , x , N, better_board[17] + Fore.WHITE)
            print(Fore.WHITE + N, one_list)
            print(Fore.WHITE + "a", N, better_board[18] + Fore.WHITE, "   " , x , N, better_board[21] + Fore.WHITE, "   " , x , N, better_board[24] + Fore.WHITE)
            print(N*2 , smol_box[6], N*2, u, smol_box[7], N*2, u, smol_box[8])
            print(Fore.WHITE + "b", N, better_board[19] + Fore.WHITE, " ", bigboard_values[6] + Fore.WHITE, x , N, better_board[22] + Fore.WHITE, " ", bigboard_values[7] + Fore.WHITE, x , N, better_board[25] + Fore.WHITE, " ", bigboard_values[8] + Fore.WHITE)
            print(N*2 , smol_box[6], N*2, u, smol_box[7], N*2, u, smol_box[8])
            print(Fore.WHITE + "c", N, better_board[20] + Fore.WHITE, "   " , x , N, better_board[23] + Fore.WHITE, "   " , x , N, better_board[26] + Fore.WHITE)
            box_to_dash()
            colour_to_no_colour()
        elif user_friendly_variable == 8:
            print(N*47, "1", N*3, "2", N*3, "3")
            print(Fore.WHITE + N, N, better_board[0] + Fore.WHITE, "   " , x , N, better_board[3] + Fore.WHITE, "   " , x , N, better_board[6] + Fore.WHITE)
            print(N*2 , smol_box[0], N*2, u, smol_box[1], N*2, u, smol_box[2])
            print(Fore.WHITE + N, N, better_board[1] + Fore.WHITE, " ", bigboard_values[0] + Fore.WHITE, x , N, better_board[4] + Fore.WHITE, " ", bigboard_values[1] + Fore.WHITE, x , N,  better_board[7], " ", bigboard_values[2] + Fore.WHITE)
            print(N*2 , smol_box[0], N*2, u, smol_box[1], N*2, u, smol_box[2])
            print(Fore.WHITE + N, N, better_board[2] + Fore.WHITE, "   " , x , N, better_board[5] + Fore.WHITE, "   " , x , N, better_board[8] + Fore.WHITE)
            print(Fore.WHITE + N, one_list)
            print(Fore.WHITE + N, N, better_board[9] + Fore.WHITE, "   " , x , N, better_board[12] + Fore.WHITE, "   " , x , N, better_board[15] + Fore.WHITE)
            print(N*2 , smol_box[3], N*2, u, smol_box[4], N*2, u, smol_box[5])
            print(Fore.WHITE + N, N, better_board[10] + Fore.WHITE, " ", bigboard_values[3] + Fore.WHITE, x , N, better_board[13] + Fore.WHITE, " ", bigboard_values[4] + Fore.WHITE, x , N, better_board[16], " ", bigboard_values[5] + Fore.WHITE) 
            print(N*2 , smol_box[3], N*2, u, smol_box[4], N*2, u, smol_box[5])
            print(Fore.WHITE + N, N, better_board[11] + Fore.WHITE, "   " , x , N, better_board[14] + Fore.WHITE, "   " , x , N, better_board[17] + Fore.WHITE)
            print(Fore.WHITE + N, one_list)
            print(Fore.WHITE + "a", N, better_board[18] + Fore.WHITE, "   " , x , N, better_board[21] + Fore.WHITE, "   " , x , N, better_board[24] + Fore.WHITE)
            print(N*2 , smol_box[6], N*2, u, smol_box[7], N*2, u, smol_box[8])
            print(Fore.WHITE + "b", N, better_board[19] + Fore.WHITE, " ", bigboard_values[6] + Fore.WHITE, x , N, better_board[22] + Fore.WHITE, " ", bigboard_values[7] + Fore.WHITE, x , N, better_board[25] + Fore.WHITE, " ", bigboard_values[8] + Fore.WHITE)
            print(N*2 , smol_box[6], N*2, u, smol_box[7], N*2, u, smol_box[8])
            print(Fore.WHITE + "c", N, better_board[20] + Fore.WHITE, "   " , x , N, better_board[23] + Fore.WHITE, "   " , x , N, better_board[26] + Fore.WHITE)
            box_to_dash()
            colour_to_no_colour()
        box_to_dash()
        

    #prints the board with numbers, when choosing fullboards or the start if the game
    def manual_print_bigboard():
        global better_board
        no_colour_to_colour()
        print_board_neatly()
        print(Fore.WHITE + N, N, better_board[0], "   " , x , N, better_board[3], "   " , x , N, better_board[6])
        print(N*2 , smol_box[0], N*2, "│ ", smol_box[1], N*2, "│ ", smol_box[2])
        print(Fore.WHITE + N, N, better_board[1], " ", "1", x , N, better_board[4], " ", "2", x , N,  better_board[7], " ", "3")
        print(N*2 , smol_box[0], N*2, "│ ", smol_box[1], N*2, "│ ", smol_box[2])
        print(Fore.WHITE + N, N, better_board[2], "   " , x , N, better_board[5], "   " , x , N, better_board[8])
        print(Fore.WHITE + N, "────────────────────┼─────────────────────┼────────────────────")
        print(Fore.WHITE + N, N, better_board[9], "   " , x , N, better_board[12], "   " , x , N, better_board[15])
        print(N*2 , smol_box[3], N*2, "│ ", smol_box[4], N*2, "│ ", smol_box[5])
        print(Fore.WHITE + N, N, better_board[10], " ", "4", x , N, better_board[13], " ", "5", x , N, better_board[16], " ", "6")
        print(N*2 , smol_box[3], N*2, "│ ", smol_box[4], N*2, "│ ", smol_box[5])
        print(Fore.WHITE + N, N, better_board[11], "   " , x , N, better_board[14], "   " , x , N, better_board[17])
        print(Fore.WHITE + N, "────────────────────┼─────────────────────┼────────────────────")
        print(Fore.WHITE + N, N, better_board[18], "   " , x , N, better_board[21], "   " , x , N, better_board[24])
        print(N*2 , smol_box[6], N*2, "│ ", smol_box[7], N*2, "│ ", smol_box[8])
        print(Fore.WHITE + N, N, better_board[19], " ", "7", x , N, better_board[22], " ", "8", x , N, better_board[25], " ", "9")
        print(N*2 , smol_box[6], N*2, "│ ", smol_box[7], N*2, "│ ", smol_box[8])
        print(Fore.WHITE + N, N, better_board[20], "   " , x , N, better_board[23], "   " , x , N, better_board[26])
        colour_to_no_colour()

    #Inputs
    #The first user input, it will determine the first board and will run a normal user input as well
    def user_input():
        global current_player
        global smol_board
        global First_Setup
        global fullvalue
        global user_friendly_variable
        global winvalue
        coord_check = 1
        columns = {"a": 0, "b": 1, "c": 2}
        rows = {"1": 0, "2": 1, "3": 2}
        #setting variables
        while First_Setup == 1:
            input_smol_board_first = input("Type what board do you want to start at, from 1-9: ")
            if len(input_smol_board_first) == 1:
                if input_smol_board_first in "123456789":
                    input_smol_board_first = int(input_smol_board_first) - 1
                    if 0 <= input_smol_board_first < 10:
                        smol_board = bigboard[input_smol_board_first]
                        user_friendly_variable = input_smol_board_first
                        clear()
                        winvalue = input_smol_board_first
                        user_friendly_print_bigboard_better()
                        #finding the small board to start on 
                        while coord_check == 1:
                            coordinate = input("Enter a coordinate: ")
                            if len(coordinate) == 2:
                                if coordinate[0] in "abc":
                                    if coordinate[1] in "123":
                                        row = rows[coordinate[1]]
                                        col = columns[coordinate[0]]
                                        if smol_board[col][row] == "-":
                                            if col < 3 and row < 3:
                                                coord_check += 1
                                                if current_player == "X":
                                                    smol_board[col][row] = "X" 
                                                    current_player = "O"
                                                    smol_board = bigboard[smol_board_dict[coordinate]]
                                                    First_Setup += 1
                                                    fullvalue = bigboard[smol_board_dict[coordinate]]
                                                    user_friendly_variable = smol_board_dict[coordinate]
                                                    winvalue = input_smol_board_first
                                                    clear()
                                                elif current_player == "O":
                                                    smol_board[col][row] = "O" 
                                                    current_player = "X"
                                                    smol_board = bigboard[smol_board_dict[coordinate]]
                                                    First_Setup += 1
                                                    fullvalue = bigboard[smol_board_dict[coordinate]]
                                                    user_friendly_variable = smol_board_dict[coordinate]
                                                    winvalue = input_smol_board_first
                                                    clear()
                                                else: 
                                                    print("Please input a valid coordinate!")
                                            else:
                                                print("Please input a valid coordinate!")
                                        else:
                                            print("Please input a valid number from 1-3!")
                                    else:
                                        print("Please input 1 lowecase letter of a, b and c and 1 number from 1-3 for a coordinate! e.g. c2")
                                elif coordinate[0] in "123":
                                    if coordinate[1] in "abc":
                                        temp_coord = (coordinate[1], coordinate[0])       
                                        new_coord = "".join(temp_coord)
                                        row = rows[new_coord[1]]
                                        col = columns[new_coord[0]]
                                        if smol_board[col][row] == "-":
                                            if col < 3 and row < 3:
                                                coord_check += 1 
                                                if current_player == "X":
                                                    smol_board[col][row] = "X" 
                                                    current_player = "O"
                                                    smol_board = bigboard[smol_board_dict[new_coord]]
                                                    First_Setup += 1
                                                    fullvalue = bigboard[smol_board_dict[new_coord]]
                                                    user_friendly_variable = smol_board_dict[new_coord]
                                                    winvalue = input_smol_board_first
                                                    clear()
                                                elif current_player == "O":
                                                    smol_board[col][row] = "O"
                                                    current_player = "X"
                                                    smol_board = bigboard[smol_board_dict[new_coord]]
                                                    First_Setup += 1
                                                    fullvalue = bigboard[smol_board_dict[new_coord]]
                                                    user_friendly_variable = smol_board_dict[new_coord]
                                                    winvalue = input_smol_board_first
                                                    clear()
                                                else: 
                                                    print("Please input a valid coordinate!")
                                            else:
                                                print("Please input a valid coordinate!")
                                        else:
                                            print("Please input a valid number from 1-3!")
                                    else:
                                        print("Please input 1 lowecase letter of a, b and c and 1 number from 1-3 for a coordinate! e.g. c2")
                                else:
                                    print("Please input a valid coordinate")
                            elif len(coordinate) == 4:
                                coordinate = coordinate.upper()
                                if coordinate == "EXIT":
                                    p = 1
                                    while p == 1:
                                        Are_sure = input("Are you sure you want to exit? Yes/No: ")
                                        Are_sure = Are_sure.upper()
                                        if Are_sure == "YES":
                                            Game()
                                        elif Are_sure == "NO":
                                            p += 1
                            else:  
                                print("Please input a valid coordinate")
                    else:
                        print("Please input a valid number from 1-9.")
                else:
                    print("Please input a valid number from 1-9.")
            elif len(input_smol_board_first) == 4:
                input_smol_board_first = input_smol_board_first.upper()
                if input_smol_board_first == "EXIT":
                    p = 1
                    while p == 1:
                        Are_sure = input("Are you sure you want to exit? Yes/No: ")
                        Are_sure = Are_sure.upper()
                        if Are_sure == "YES":
                            Game()
                        elif Are_sure == "NO":
                            p += 1
            else:
                print("Please input a valid number from 1-9.")

    #user inputs for the later game
    def user_input2():
        global full_board
        global current_player
        global smol_board
        global winvalue
        global loop_of_full
        global coordinate
        global fullvalue
        global user_friendly_variable
        full_board_with_win()
        coordinate = input(f'{current_player}, enter a coordinate: ')  
        if len(coordinate) == 2:
            if coordinate[0] in "abc":
                if coordinate[1] in "123":
                    if len(coordinate) == 2:    
                        row = rows[coordinate[1]]
                        col = columns[coordinate[0]]
                        if smol_board[col][row] == "-":
                            if col < 3 and row < 3:
                                if current_player == "X":
                                    smol_board[col][row] = "X"
                                    current_player = "O"
                                    smol_board_wincheck()
                                    winvalue = smol_board_dict[coordinate]
                                    fullvalue = bigboard[smol_board_dict[coordinate]]
                                    smol_board = bigboard[smol_board_dict[coordinate]]
                                    user_friendly_variable = smol_board_dict[coordinate]
                                    full_board = 1
                                elif current_player == "O":
                                    smol_board[col][row] = "O" 
                                    current_player = "X"
                                    smol_board_wincheck()
                                    winvalue = smol_board_dict[coordinate]
                                    fullvalue = bigboard[smol_board_dict[coordinate]]
                                    smol_board = bigboard[smol_board_dict[coordinate]]
                                    user_friendly_variable = smol_board_dict[coordinate]
                                    full_board = 1
                                else:
                                    print("Please choose a valid coordinate.")
                            else:
                                print("Please choose a valid coordinate.")
                        else:
                            print("Please choose a valid coordinate.")
                    else:
                        print("Please choose a valid coordinate.")
                else:
                    print("Please choose a valid coordinate.")
            elif coordinate[0] in "123":
                if coordinate[1] in "abc":
                    if len(coordinate) == 2:
                        temp_coord = (coordinate[1], coordinate[0])       
                        new_coord = "".join(temp_coord)
                        row = rows[new_coord[1]]
                        col = columns[new_coord[0]]
                        if smol_board[col][row] == "-":
                            if col < 3 and row < 3:
                                if current_player == "X":
                                    smol_board[col][row] = "X"
                                    current_player = "O"
                                    smol_board_wincheck()
                                    winvalue = smol_board_dict[new_coord]
                                    fullvalue = bigboard[smol_board_dict[new_coord]]
                                    smol_board = bigboard[smol_board_dict[new_coord]]
                                    user_friendly_variable = smol_board_dict[new_coord]
                                    full_board = 1
                                elif current_player == "O":
                                    smol_board[col][row] = "O"
                                    current_player = "X"
                                    smol_board_wincheck()
                                    winvalue = smol_board_dict[new_coord]
                                    fullvalue = bigboard[smol_board_dict[new_coord]]
                                    smol_board = bigboard[smol_board_dict[new_coord]]
                                    user_friendly_variable = smol_board_dict[new_coord]
                                    full_board = 1
                                else:
                                    print("Please choose a valid coordinate.")
                            else:
                                print("Please choose a valid coordinate.")
                        else:
                            print("Please choose a valid coordinate.")
                    else:
                        print("Please choose a valid coordinate.")
                else:
                    print("Please choose a valid coordinate.")
            else: 
                print("Please enter a valid coordinate.")
        elif len(coordinate) == 4:
            coordinate = coordinate.upper()
            if coordinate == "EXIT":
                p = 1
                while p == 1:
                    Are_sure = input("Are you sure you want to exit? Yes/No: ")
                    Are_sure = Are_sure.upper()
                    if Are_sure == "YES":
                        Game()
                    elif Are_sure == "NO":
                        p += 1
        else:
            print("Please input a coordinate")


    def user_input2_ai():
        global full_board
        global current_player
        global smol_board
        global winvalue
        global loop_of_full
        global coordinate
        global fullvalue
        global user_friendly_variable
        global not_valid
        full_board_with_win()
        not_valid = 1
        while not_valid == 1:
            coordinate = input(f'{current_player}, enter a coordinate: ')  
            if len(coordinate) == 2:
                if coordinate[0] in "abc":
                    if coordinate[1] in "123":
                        if len(coordinate) == 2:    
                            row = rows[coordinate[1]]
                            col = columns[coordinate[0]]
                            if smol_board[col][row] == "-":
                                if col < 3 and row < 3:
                                    not_valid += 1 
                                    if current_player == "X":
                                        smol_board[col][row] = "X"
                                        current_player = "O"
                                        smol_board_wincheck()
                                        winvalue = smol_board_dict[coordinate]
                                        fullvalue = bigboard[smol_board_dict[coordinate]]
                                        smol_board = bigboard[smol_board_dict[coordinate]]
                                        user_friendly_variable = smol_board_dict[coordinate]
                                        full_board = 1
                                        smol_board_wincheck()
                                    elif current_player == "O":
                                        smol_board_wincheck()
                                        smol_board[col][row] = "O"
                                        current_player = "X"
                                        smol_board_wincheck()
                                        winvalue = smol_board_dict[coordinate]
                                        fullvalue = bigboard[smol_board_dict[coordinate]]
                                        smol_board = bigboard[smol_board_dict[coordinate]]
                                        user_friendly_variable = smol_board_dict[coordinate]
                                        full_board = 1
                                        smol_board_wincheck()
                                    else:
                                        print("Please choose a valid coordinate.")
                                else:
                                    print("Please choose a valid coordinate.")
                            else:
                                print("Please choose a valid coordinate.")
                        else:
                            print("Please choose a valid coordinate.")
                    else:
                        print("Please choose a valid coordinate.")
                elif coordinate[0] in "123":
                    if coordinate[1] in "abc":
                        if len(coordinate) == 2:
                            temp_coord = (coordinate[1], coordinate[0])       
                            new_coord = "".join(temp_coord)
                            row = rows[new_coord[1]]
                            col = columns[new_coord[0]]
                            if smol_board[col][row] == "-":
                                if col < 3 and row < 3:
                                    not_valid += 1 
                                    if current_player == "X":
                                        smol_board_wincheck()
                                        smol_board[col][row] = "X"
                                        current_player = "O"
                                        smol_board_wincheck()
                                        winvalue = smol_board_dict[new_coord]
                                        fullvalue = bigboard[smol_board_dict[new_coord]]
                                        smol_board = bigboard[smol_board_dict[new_coord]]
                                        user_friendly_variable = smol_board_dict[new_coord]
                                        full_board = 1
                                        smol_board_wincheck()
                                    elif current_player == "O":
                                        smol_board_wincheck()
                                        smol_board[col][row] = "O"
                                        current_player = "X"
                                        smol_board_wincheck()
                                        winvalue = smol_board_dict[new_coord]
                                        fullvalue = bigboard[smol_board_dict[new_coord]]
                                        smol_board = bigboard[smol_board_dict[new_coord]]
                                        user_friendly_variable = smol_board_dict[new_coord]
                                        full_board = 1
                                        smol_board_wincheck()
                                    else:
                                        print("Please choose a valid coordinate.")
                                else:
                                    print("Please choose a valid coordinate.")
                            else:
                                print("Please choose a valid coordinate.")
                        else:
                            print("Please choose a valid coordinate.")
                    else:
                        print("Please choose a valid coordinate.")
                else: 
                    print("Please enter a valid coordinate.")
            elif len(coordinate) == 4:
                coordinate = coordinate.upper()
                if coordinate == "EXIT":
                    p = 1
                    while p == 1:
                        Are_sure = input("Are you sure you want to exit? Yes/No: ")
                        Are_sure = Are_sure.upper()
                        if Are_sure == "YES":
                            Game()
                        elif Are_sure == "NO":
                            p += 1
            else:
                print("Please input a coordinate")

    #Not an AI, but random moves. "What a scam" you may think. Yep. It is. You can clearly see from this that I am out of ideas and very tired.

    #The ai that is player O
    def AIMoves_O():
        global current_player
        global AI
        global smol_board
        global Variable_ender
        global fullvalue
        global coordinate
        global user_friendly_variable
        global winvalue
        EmptyPositionAI = False
        while EmptyPositionAI is False:
            bigboard_board_wincheck()
            full_board_with_win_ai()
            AIsymbolposition = random.randint(0, 2)
            AIsymbolposition2 = random.randint(0, 2)
            if smol_board[AIsymbolposition][AIsymbolposition2] == "-":
                EmptyPositionAI = True
                AIcoord = columns_ai[AIsymbolposition]
                AIcoord1 = rows_ai[AIsymbolposition2]
                ai_input = [AIcoord, AIcoord1]
                coordinate = "".join(ai_input)
                smol_board[AIsymbolposition][AIsymbolposition2] = current_player
                smol_board_wincheck()
                current_player = "X"
                smol_board_wincheck()
                winvalue = smol_board_dict[coordinate]
                fullvalue = bigboard[smol_board_dict[coordinate]]
                smol_board = bigboard[smol_board_dict[coordinate]]
                user_friendly_variable = smol_board_dict[coordinate]
                full_board = 1  
                smol_board_wincheck()

    #The ai that is player X
    def AIMoves_X():
        global current_player
        global AI
        global smol_board
        global Variable_ender
        global fullvalue
        global coordinate
        global user_friendly_variable
        global winvalue
        if Variable_ender == 0:
            random_variable = random.randint(0, 8)
            smol_board = bigboard[random_variable]
            fullvalue = bigboard[random_variable] 
        if Variable_ender == 1 or Variable_ender == 0:
            Variable_ender += 1
        EmptyPositionAI = False
        while EmptyPositionAI is False:
            bigboard_board_wincheck()
            full_board_with_win_ai()
            AIsymbolposition = random.randint(0, 2)
            AIsymbolposition2 = random.randint(0, 2)
            if smol_board[AIsymbolposition][AIsymbolposition2] == "-":
                EmptyPositionAI = True
                AIcoord = columns_ai[AIsymbolposition]
                AIcoord1 = rows_ai[AIsymbolposition2]
                ai_input = [AIcoord, AIcoord1]
                coordinate = "".join(ai_input)
                smol_board[AIsymbolposition][AIsymbolposition2] = current_player
                if Variable_ender == 1:
                    winvalue = smol_board_dict[coordinate]
                smol_board_wincheck()
                current_player = "O"
                smol_board_wincheck()
                winvalue = smol_board_dict[coordinate]
                fullvalue = bigboard[smol_board_dict[coordinate]]
                smol_board = bigboard[smol_board_dict[coordinate]]
                user_friendly_variable = smol_board_dict[coordinate]
                full_board = 1
                smol_board_wincheck()

    #Gameplay functions
    #All of the functions put into one function for the game to work.
    def Functioning_game_player_vs_player():
        global loop_of_game
        manual_print_bigboard()
        user_input()
        user_friendly_print_bigboard_better()
        while infiloop == 1:
            if loop_of_game is True:
                user_input2()
                clear()
                bigboard_board_wincheck()
                if loop_of_game is True:
                    user_friendly_print_bigboard_better()
            elif loop_of_game is False:
                time.sleep(20)
                Game()

    #Player is O, random is X
    def Functioning_game_ai_X():
        global loop_of_game
        AIMoves_X()
        user_friendly_print_bigboard_better()
        user_input2_ai()
        clear()
        user_friendly_print_bigboard_better()
        while infiloop == 1:
            if loop_of_game is True:
                clear()
                AIMoves_X()
                bigboard_board_wincheck()
                if loop_of_game is True:
                    clear()
                    user_friendly_print_bigboard_better()
                    user_input2_ai()  
                    clear()
                    bigboard_board_wincheck()
            elif loop_of_game is False:
                time.sleep(20)
                Game()
                

    #Player is X, random is O
    def Functioning_game_ai_O():
        global loop_of_game
        manual_print_bigboard()
        user_input()
        user_friendly_print_bigboard_better()
        AIMoves_O()
        clear()
        user_friendly_print_bigboard_better()
        while infiloop == 1:
            if loop_of_game is True:
                user_input2_ai()
                clear()
                bigboard_board_wincheck()
                if loop_of_game is True:
                    AIMoves_O()
                    bigboard_board_wincheck()
                    if loop_of_game is True:
                        clear()
                        user_friendly_print_bigboard_better()
            elif loop_of_game is False:
                time.sleep(20)
                Game()

    #User input at the start, allows the user to start the game.
    def Gameplay():
        while infiloop == 1:
            print("Hello! Welcome to my game of recursive tictactoe / ultimate tictactoe. \n")
            print("During this game, at any time you can type 'exit' to exit the current game.\n")
            user_decision_ai_or_player = input("Please choose between 'Player vs Random AI' or 'Player vs Player': ")
            user_decision_ai_or_player = user_decision_ai_or_player.upper()
            if user_decision_ai_or_player == "PLAYER VS PLAYER":
                user_decision = input("Enter 'X' or 'O' Player 1: ")
                player1 = user_decision
                if player1 == "X":
                    player2 = "O"
                    clear()
                    print(Fore.WHITE, "Player 1 is" + " ", Fore.WHITE, end=""), print(Fore.RED + player1 + Fore.WHITE)
                    print(Fore.WHITE, "Player 2 is" + " ", Fore.WHITE, end=""), print(Fore.BLUE + player2 + Fore.WHITE)
                    print("\n")
                    Functioning_game_player_vs_player()
                elif player1 == "O":
                    player2 = "X"
                    clear()
                    print(Fore.WHITE, "Player 1 is" + " ", Fore.WHITE, end=""), print(Fore.BLUE + player1, Fore.WHITE)
                    print(Fore.WHITE, "Player 2 is" + " ", Fore.WHITE, end=""), print(Fore.RED, player2, Fore.WHITE)
                    print("\n")
                    Functioning_game_player_vs_player()
            elif user_decision_ai_or_player == "PLAYER VS RANDOM AI":
                user_decision = input("Are you going to play as X or O?: ")
                if user_decision == "X":
                    clear()
                    Functioning_game_ai_O()
                elif user_decision == "O":
                    clear()
                    Functioning_game_ai_X()
                else: 
                    clear()
                    print("That is not a valid input")
            else:
                clear()
                print("That is not a valid input.")
                print("\n")

    #Runs the code
    Gameplay()

def Game():
    global Variable
    if Variable == 1:
        Blank = input("Ready to run the program? ")
        Blank = Blank.upper()
        if Blank == "YES":
            Variable += 1
            clear()
            Recursive_Tictactoe()
        elif Blank == "NO":
            exit()
        else:
            print("If you got here and you are not me then don't worry about this.")
    elif Variable == 2:
        clear()
        Recursive_Tictactoe()
    else:
        print("Sorry something broke. This isn't supposed to happen at all.")

Game()