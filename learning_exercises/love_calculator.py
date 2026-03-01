# Love Calculator
my_name = input("What is your name? ")
her_name  = input("What is his/her name? ")

couple = my_name + " " + her_name
lowercase_couple = couple.lower()
print(couple)

t = lowercase_couple.count("t")
r = lowercase_couple.count("r")
u = lowercase_couple.count("u")
e = lowercase_couple.count("e")
true = str(t+r+u+e)

l = lowercase_couple.count("l")
o = lowercase_couple.count("o")
v = lowercase_couple.count("v")
e = lowercase_couple.count("e")
love = str(l+o+v+e)

love_percentage = int(true + love)

if love_percentage < 10 or love_percentage > 90:
    print(f"Your love score is {love_percentage} and you go together like coke and mentos!")
elif 40 <= love_percentage <= 50:
    print(f"Your love score is {love_percentage} and you are alright together!")
else:
    print(f"Your love score is {love_percentage}")
