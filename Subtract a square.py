# Subtract a square game
# Author  : Kareem Magdy
# Date    : 25 Feb. 2022
# Version : 1.0

# please note that subtraction operation has 3 operatives ( Minuend - Subtrahend = Difference )

def gameBoard():
    board = [1, 4, 9, 16, 25, 36, 49, 64]
    return board


def player_1(player_list1, minuend):
    for i in player_list1:
        print(i, end="    ")
    player1_choice = int(input("\nPlayer one turn\nChoose a number : "))

    if player1_choice in player_list1:
        if minuend - player1_choice == 0:
            print("Total now is ", minuend - player1_choice)
            print("-------------------------------------------")
            print("\nPlayer one wins")
        elif minuend - player1_choice < 0:
            print("ERROR , choose another number")
            print("-------------------------------------------")
            player_1(player_list1, minuend)
        else:
            print("Total now is ", minuend - player1_choice)
            print("-------------------------------------------")
            player_2(player_list1, minuend - player1_choice)
    else:
        print("-------------------------------------------")
        print("Error, choose a number from the list ")
        player_1(player_list1, minuend)


def player_2(player_list2, minuend):
    for i in player_list2:
        print(i, end="    ")
    player2_choice = int(input("\nPlayer two turn\nChoose a number : "))

    if player2_choice in player_list2:
        if minuend - player2_choice == 0:
            print("\nTotal now is ", minuend - player2_choice)
            print("-------------------------------------------")
            print("\nPlayer two wins")
        elif minuend - player2_choice < 0:
            print("ERROR , choose another number")
            print("-------------------------------------------")
            player_2(player_list2, minuend)
        else:
            print("\nTotal now is ", minuend - player2_choice)
            print("-------------------------------------------")
            player_1(player_list2, minuend - player2_choice)
    else:
        print("-------------------------------------------")
        print("Error, choose a number from the list")
        player_2(player_list2, minuend)

print("Welcome to subtract a square game")

print("-------------------------------------------")
print("please note that subtraction operation has 3 operatives ( Minuend - Subtrahend = Difference )")
player_1(gameBoard(), int(input("Input a minuend to start the game :")))
