# Let's play rock paper scissors

from random import randint

user_choice = int(input("Make a choice: 0-Rock, 1-Paper, 2-Scissors: "))
comps_choice = randint(0, 2)
choices = ["Rock", "Paper", "Scissors"]

if user_choice < 0 or user_choice > 2:
    print("Invalid choice. Please enter 0, 1, or 2.")
else:
    print(f"You chose {choices[user_choice]}, computer chose {choices[comps_choice]}")

    if user_choice == comps_choice:
        print("It's a tie!")
    elif user_choice == 0 and comps_choice == 2:
        print("Rock crushes Scissors — you WIN!")
    elif user_choice == 2 and comps_choice == 0:
        print("Scissors lost to Rock — you LOSE!")
    elif user_choice > comps_choice:
        print("You WIN!")
    elif user_choice < comps_choice:
        print("You LOSE!")

