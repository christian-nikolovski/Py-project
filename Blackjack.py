import random 
import time

global loop_check

def blackjack():

    ending_first_check = 1
    t = 1
    loop_check = 1
    player_card_5 = 100

    Spades = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    Clubs = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    Hearts = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    Diamonds = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    Cards = ["Spades", "Clubs", "Hearts", "Diamonds"]

    empty_list = []
    player_list = []
    T_or_F_list = []
    ending_numbers = []
    player_ace_list = []

    card_dict = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}
    player_dict = {}

    def n_o_players(smol_number_of_players):
        if smol_number_of_players > 8:
            print("You cannot choose more than 8 players")
        elif 0 >= smol_number_of_players:
            print("You cannot choose 0 or less players")
        elif 0 < smol_number_of_players <= 8:
            for i in range(smol_number_of_players):
                player_list.append([])
                player_number = i
                card_choosing(player_list[player_number])
                card_choosing(player_list[player_number])
                T_or_F_list.append(True)
                player_dict.update({"Player " + str(i+1) : 0})
                player_ace_list.append(["Ace of Spades", "Ace of Clubs", "Ace of Hearts", "Ace of Diamonds"])
            player_list.append([])
            card_choosing(player_list[-1])
            card_choosing(player_list[-1])
            player_ace_list.append(["Ace of Spades", "Ace of Clubs", "Ace of Hearts", "Ace of Diamonds"])
            player_dict.update({"Dealer" : 0})
            
    def clear():
        print("\033[H\033[J") 

    def card_choosing(list):
        x = "a"
        y = "a"
        if len(Cards) != 0:
            x = random.choice(Cards)
            if x == "Spades":
                if len(Spades) != 0:
                    y = random.choice(Spades)
                    Spades.remove(y)
                    appended_list_func = (y + " of " + x)
                    list.append(appended_list_func)
                else:
                    Cards.remove("Spades")
            elif x == "Clubs":
                if len(Clubs) != 0:
                    y = random.choice(Clubs)
                    Clubs.remove(y)
                    appended_list_func = (y + " of " + x)
                    list.append(appended_list_func)
                else:
                    Cards.remove("Clubs")
            elif x == "Hearts":
                if len(Hearts) != 0:
                    y = random.choice(Hearts)
                    Hearts.remove(y)
                    appended_list_func = (y + " of " + x)
                    list.append(appended_list_func)
                else:
                    Cards.remove("Hearts")
            elif x == "Diamonds":
                if len(Diamonds) != 0:
                    y = random.choice(Diamonds)
                    Diamonds.remove(y)
                    appended_list_func = (y + " of " + x)
                    list.append(appended_list_func)
                else:
                    Cards.remove("Diamonds")

    def gameplay():
        global loop_check
        global player_number
        global player_boolean
        global print_player
        global number_of_players
        for i in range(int(number_of_players)):
            loop_check = 1
            player_number = i
            player_boolean = T_or_F_list[player_number]
            print_player = i + 1
            if player_boolean == True:  
                if int(number_of_players) != 1:
                    more_than_1_player()
                elif int(number_of_players) == 1:
                    _1_player()

    def _1_player():
        def gameplay__1_player():
            global loop_check
            global player_number
            global player_boolean
            global print_player
            while loop_check == 1:
                clear()
                print("Dealer cards:")
                print("")
                print(player_list[-1][0])
                print("")
                print("###########")
                print("")
                print("Player cards:")
                print("")
                for i in player_list[player_number]:
                    print(i)
                    print()
                player_dict_var = "Player " + str(player_number + 1)
                total_player_number = player_dict[player_dict_var]
                if total_player_number == 0:
                    _1_player_cardcheck(player_number)
                    player_boolean = T_or_F_list[player_number]
                if player_boolean == True:
                    H_or_S = input(f'Hit or Stand?: ')
                    H_or_S = H_or_S.upper()
                    if H_or_S == "HIT":
                        Y_or_N_S = input("Are you sure you want to hit? You will get another card in your list of cards. Yes or No: ")
                        Y_or_N_S = Y_or_N_S.upper()
                        if Y_or_N_S == "YES":
                            card_choosing(player_list[player_number])
                            print("")
                            print(player_list[player_number][-1])
                            print("")
                            _1_player_cardcheck(player_number)
                            time.sleep(1)
                            clear()
                            loop_check = 2
                            total_player_number = player_dict[player_dict_var]
                            if len(player_list[player_number]) == 5:
                                if total_player_number <= 21:
                                    for i in range(int(number_of_players)):
                                        T_or_F_list[i] = False
                        elif Y_or_N_S == "NO":
                            pass
                        else:
                            print("")
                            print("That is not a valid input! Sending you back to first choosing...")
                            time.sleep(1)
                    elif H_or_S == "STAND":
                        Y_or_N_S = input("Are you sure you want to stand? It means you will no longer get the option to hit, and your turn will be skipped. Yes or No: ")
                        Y_or_N_S = Y_or_N_S.upper()
                        if Y_or_N_S == "YES":
                            T_or_F_list[player_number] = False
                            loop_check = 2
                            clear()
                        elif Y_or_N_S == "NO":
                            pass
                        else:
                            print("")
                            print("That is not a valid input! Sending you back to first choosing...")
                            time.sleep(1)
                    else:
                        print("")
                        print("That is not a valid input! Sending you back to first choosing...")
                        time.sleep(1)
                if player_boolean == False:
                    loop_check = 2

        def _1_player_cardcheck(player_number):
            player_dict_var = "Player " + str(player_number + 1)
            total_player_number = player_dict[player_dict_var]
            number_of_items = int(len(player_list[player_number]))
            player_item_list = []
            if total_player_number == 0:
                for x in range(number_of_items):  
                    player_item = player_list[player_number][x].split(" ")
                    card_number = card_dict[player_item[0]]
                    total_player_number_new = card_dict[player_item[0]] + total_player_number
                    player_dict[player_dict_var] = total_player_number_new
                    total_player_number = player_dict[player_dict_var]
            else:
                player_item = player_list[player_number][-1].split(" ")
                card_number = card_dict[player_item[0]]
                total_player_number_new = card_number + total_player_number
                player_dict[player_dict_var] = total_player_number_new
            total_player_number = player_dict[player_dict_var]
            if total_player_number == 21:
                print("Blackjack!")
                T_or_F_list[player_number] = False
            elif total_player_number > 21:
                for x in player_list[player_number]:
                    for y in player_ace_list[player_number]:
                        if x == y:
                            total_player_number = total_player_number - 10
                            player_ace_list[player_number].remove(y)
                            player_dict[player_dict_var] = total_player_number
                            total_player_number = player_dict[player_dict_var]
                            if total_player_number < 21:
                                if total_player_number == 21:
                                    print("Blackjack!")
                                    T_or_F_list[player_number] = False
                                    break
                                break

                if total_player_number > 21:
                    print("Bust! You lose.")
                    T_or_F_list[player_number] = False

        gameplay__1_player()

    def more_than_1_player():
        def gameplay__more_than_1_player():
            global loop_check
            global player_number
            global player_boolean
            global print_player
            input(f'Player {print_player}s turn. Swivel the computer to player {print_player}. Press enter once this is done. ')
            while loop_check == 1:
                clear()
                print("Dealer cards:")
                print("")
                print(player_list[-1][0])
                print("")
                print("###########")
                print("")
                print("Player cards:")
                print("")
                for i in player_list[player_number]:
                    print(i)
                    print()
                player_dict_var = "Player " + str(player_number + 1)
                total_player_number = player_dict[player_dict_var]
                if total_player_number == 0:
                    more_than_1_player_card_check(player_number)
                    player_boolean = T_or_F_list[player_number]
                if player_boolean == True:
                    H_or_S = input(f'Player {print_player} - Hit or Stand?: ')
                    H_or_S = H_or_S.upper()
                    if H_or_S == "HIT":
                        Y_or_N_S = input("Are you sure you want to hit? You will get another card in your list of cards. Yes or No: ")
                        Y_or_N_S = Y_or_N_S.upper()
                        if Y_or_N_S == "YES":
                            card_choosing(player_list[player_number])
                            print("")
                            print(player_list[player_number][-1])
                            print("")
                            more_than_1_player_card_check(player_number)
                            time.sleep(1)
                            clear()
                            loop_check = 2
                            total_player_number = player_dict[player_dict_var]
                            if len(player_list[player_number]) == 5:
                                if total_player_number <= 21:
                                    for i in range(int(number_of_players)):
                                        T_or_F_list[i] = False
                        else:
                            print("")
                            print("That is not a valid input! Sending you back to first choosing...")
                            time.sleep(1)
                    elif H_or_S == "STAND":
                        Y_or_N_S = input("Are you sure you want to stand? It means you will no longer get the option to hit, and your turn will be skipped. Yes or No: ")
                        Y_or_N_S = Y_or_N_S.upper()
                        if Y_or_N_S == "YES":
                            T_or_F_list[player_number] = False
                            loop_check = 2
                            clear()
                        else:
                            print("")
                            print("That is not a valid input! Sending you back to first choosing...")
                            time.sleep(1)
                    else:
                        print("")
                        print("That is not a valid input! Sending you back to first choosing...")
                        time.sleep(1)
                if player_boolean == False:
                    loop_check = 2
            

        def more_than_1_player_card_check(player_number):
            player_dict_var = "Player " + str(player_number + 1)
            total_player_number = player_dict[player_dict_var]
            number_of_items = int(len(player_list[player_number]))
            player_item_list = []
            if total_player_number == 0:
                for x in range(number_of_items):  
                    player_item = player_list[player_number][x].split(" ")
                    card_number = card_dict[player_item[0]]
                    total_player_number_new = card_number + total_player_number
                    player_dict[player_dict_var] = total_player_number_new
                    total_player_number = player_dict[player_dict_var]
            else:
                player_item = player_list[player_number][-1].split(" ")
                card_number = card_dict[player_item[0]]
                total_player_number_new = card_number + total_player_number
                player_dict[player_dict_var] = total_player_number_new
            total_player_number = player_dict[player_dict_var]
            if total_player_number == 21:
                print("Blackjack!")
                T_or_F_list[player_number] = False
            elif total_player_number > 21:
                for x in player_list[player_number]:
                    for y in player_ace_list[player_number]:
                        if x == y:
                            total_player_number = total_player_number - 10
                            player_ace_list[player_number].remove(y)
                            player_dict[player_dict_var] = total_player_number
                            total_player_number = player_dict[player_dict_var]
                            if total_player_number < 21:
                                if total_player_number == 21:
                                    print("Blackjack!")
                                    T_or_F_list[player_number] = False
                                    break
                                break

                if total_player_number > 21:
                    print("Bust! You lose.")
                    print("Your turn will be skipped from now on.")
                    T_or_F_list[player_number] = False
        gameplay__more_than_1_player()

    def dealer_cards():
        player_dict_var = "Dealer"
        number_of_items = int(len(player_list[-1]))
        total_player_number = player_dict[player_dict_var]
        for x in range(number_of_items):  
            player_item = player_list[-1][x].split(" ")
            card_number = card_dict[player_item[0]]
            total_player_number_new = card_dict[player_item[0]] + total_player_number
            player_dict[player_dict_var] = total_player_number_new
            total_player_number = player_dict[player_dict_var]
        total_player_number = player_dict[player_dict_var]
        while total_player_number < 17:
            card_choosing(player_list[-1])
            player_item = player_list[-1][-1].split(" ")
            card_number = card_dict[player_item[0]]
            total_player_number_new = card_number + total_player_number
            player_dict[player_dict_var] = total_player_number_new
            total_player_number = player_dict[player_dict_var]
            if total_player_number > 21:
                for x in player_list[-1]:
                    for y in player_ace_list[-1]:
                        if x == y:
                            total_player_number = total_player_number - 10
                            player_ace_list[-1].remove(y)
                            player_dict[player_dict_var] = total_player_number
                            total_player_number = player_dict[player_dict_var]
                            if total_player_number < 21:
                                break
                if total_player_number > 21:
                    break

    def end():
        global player_card_5
        global number_of_players
        player_card_5 = 100
        dealer_cards()
        for x in player_list:
            if len(x) == 5:
                player_card_5 = x
                player_num_5 = player_list.index(player_card_5)      
                if number_of_players == player_num_5:
                    player_num_5 = "Dealer"
                    if player_dict["Dealer"] > 21:
                        player_card_5 = 100
                        break
                else:
                    player_num_5 = list(player_dict)[player_num_5]
                    if player_dict[player_num_5] > 21:
                        player_card_5 = 100
                        break
        if player_card_5 == 100:
            max_value = max(player_dict.values())
            winner_list = []
            for p_name in player_dict.keys():
                if player_dict[p_name] == max_value:
                    winner_list.append(str(p_name))
            while max_value > 21:
                for i in winner_list:
                    player_dict[i] = 0
                max_value = max(player_dict.values())
                winner_list = []
                for p_name in player_dict.keys():
                    if player_dict[p_name] == max_value:
                        winner_list.append(str(p_name))
                if max_value == 0:
                    winner_list = []
                    break

        if player_card_5 != 100:
            print("The winner of the game is: ", end="")
            print(f"{player_num_5}", end=" ")
            print("congratulations to the winner!")
            print("They won by getting 5 cards without busting!")

        elif number_of_players != 1:
            if len(winner_list) > 1:
                print("The winners of the game are: ", end="")
                for x in winner_list:
                    print(x + ", ", end="")
                print("congratulations to the winners!")
                print(f"They all won with {max_value}")
            elif len(winner_list) == 1:
                print("The winner of the game is: ")
                for x in winner_list:
                    print(x + ", ", end="")
                    print("congratulations to the winner!")
                    print(f"They won with {max_value}")
            else:
                print("Nobody won!")
                print("Everyone busted!")
        while True:
            play_again = input("Play again? Yes/No: ").upper()
            if play_again == "NO":
                exit()
            elif play_again == "YES":
                clear()
                blackjack()
            else:
                clear()
                print("That is not a valid input.")

    def start():
        global number_of_players
        global smol_number_of_players
        print("Welcome to blackjack!")
        number_of_players = input("Please choose the number of players in this game, from 1-8: ")
        n_o_players(int(number_of_players))
        while True in T_or_F_list:
            gameplay()
        if True not in T_or_F_list:
            end()



    start()

blackjack()