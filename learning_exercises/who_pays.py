# You ate food in a hotel with friends,
# you give out your cards and one is picked to pay everyone's bill.

import random
names = input("Please enter everyone's name separated by a comma: ")
names_list = names.split(",")

# who_pays = random.choice(names_list) --- This is the obvious method
len_names_list = len(names_list)
who_pays = random.randint(0, len_names_list-1) # randint includes the second number
print(f"{names_list[who_pays].upper()} will pay the bill.")
