#Import the random package
import random

#Generate a random digit 0-2
int = random.randint(0, 2)

#Define the options(rock, paper, scissors)
optns = ["Rock", "Paper", "Scissors"]

# Initialize a player input
player = False

#Start the game
while player == False:
    #User input to pick an option
    player = input("Rock, Paper, or Scissors?\n")

    #Not in list
    if player not in optns:
        player = input("Some kind of wise guy? Try again.\n")

    #Same
    elif player == optns[int]:
        print("Tie!")

    #Player picks rock
    elif player == "Rock":
        if optns[int] == "Paper":
            print("You lose!", optns[int], "covers", player)
        else:
            print("You win!", player, "breaks", optns[int])

    #Player picks paper
    elif player == "Paper":
        if optns[int] == "Scissors":
            print("You lose!", optns[int], "cuts", player)
        else:
            print("You win!", player, "covers", optns[int])

    #Player picks scissors
    elif player == "Scissors":
        if optns[int] == "Paper":
            print("You win!", player, "cuts", optns[int])
