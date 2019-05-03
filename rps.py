# practice making a rock paper scissors program for interview
import sys, random

def main():
    options = {"rock", "paper", "scissors"}

    player_choice = input("Choose rock, paper, or scissors: ")
    player_choice = player_choice.lower()

    while player_choice not in options:
        player_choice = input("Please choose rock, paper, or scissors: ")

    comp_choice = random.sample(options, 1)[0]

    if player_choice == comp_choice:
        print("You tied!")
        main()

    elif (player_choice == "rock" and comp_choice == "scissors" or 
        player_choice == "paper" and comp_choice == "rock" or
        player_choice == "scissors" and comp_choice == "paper"):

        print("YOU WIN!\nYou chose {0}\nComputer chose {1}\n{0} beats {1}".format(player_choice, comp_choice))

    else:
        print("Sorry, you lose!\nYou chose {0}\nComputer chose {1}\n{1} beats {0}".format(player_choice, comp_choice))

if __name__ == "__main__":
    main()