# Let's play rock paper scissors

from random import randint

user_choice = int(input("Make a choice: 0-ROCK, 1-PAPER, 2-SCISSORS: "))
print(user_choice)
comps_choice = randint(0,2)
print(comps_choice)

if 3 <= user_choice < 0:
    print("You entered an invalid number. YOU LOSE!")
else:
    if user_choice == comps_choice:
        print("It's a tie. Rock again!")
    elif user_choice == 0 and comps_choice == 2:
        print("Yaaaaay! You've WON!")
    elif user_choice == 2 and comps_choice == 0:
        print("Ooopse! YOU LOST!")
    elif user_choice > comps_choice:
        print("Yaaaaay! You've WON!")
    elif user_choice < comps_choice:
        print("Ooopse! YOU LOST!")

