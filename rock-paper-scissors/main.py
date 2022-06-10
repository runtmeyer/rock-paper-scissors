import random

while True:
    player = input("Enter a choice ( R for rock, P for paper, S for scissors): ")

    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {player}, computer chose {computer_action}.\n")

    if player == computer_action:
        print(f"Both players selected {player}. It's a tie!")
    elif player == "R":
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player == "S":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break