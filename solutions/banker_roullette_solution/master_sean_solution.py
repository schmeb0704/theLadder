import random

print("Names must be entered like this: Angela, Ben, Jenny, Michael, Chloe")
names_input = input("Write the names of your friends: ")
names = names_input.split(", ")
random_index = random.randrange(0, len(names))


print(f"{names[random_index]} is going to buy the meal today!")