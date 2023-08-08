# Banker Roulette
# This is the start of the code

import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma: \n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆


# Write your code below this line 👇
name_list = []
name_list.append(names_string)

random_ind = random.randrange(len(names))
random_name = names[random_ind]
print(str(random_name).title() + " is going to buy the meal today!")

# Write your code above this line 👆
