import random
choice = int(input("Choose: Heads(1) or tails(2): "))

heads_tails = random.randint(1,2)
print(heads_tails)
if choice == heads_tails:
    print("You are a GAMBLER!")
else:
    print("Try again. All the best!")
print("Good bye! See you in the next round!")

