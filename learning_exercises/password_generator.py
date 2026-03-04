import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []

print("=" * 70)
print("Welcome To Password Generator")
print("=" * 70)

n_letters = int(input("How many letters do you want in your password?\n"))
n_symbols = int(input("How many symbols do you want in your password?\n"))
n_numbers = int(input("How many numbers do you want in your password?\n"))

for n in range(1, n_letters+1):
    pwd = random.choice(letters)
    password.append(pwd)
for n in range(1, n_symbols+1):
    pwd = random.choice(symbols)
    password.append(pwd)
for n in range(1, n_numbers+1):
    pwd = random.choice(numbers)
    password.append(pwd)

# print(password) # This will be a list in a general order so it is an easy to crack password it is also 
# not that readable so it is better to convert the list to a string

random.shuffle(password)
shuffled_password = ''
for i in password:
    shuffled_password += i

print(f"Your strong password is: {shuffled_password}")

# Printing an uppercase and lowercase string list of alphabet
# import string
#
# alphabet_list = list(string.ascii_letters)
# print(alphabet_list)
