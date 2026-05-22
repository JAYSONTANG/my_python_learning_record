message = "Welcome! What Chinese food do you want to eat: "
message += "\nIf you don't want to eat right now, please enter 'quit'."

Chinese_food = ""
while Chinese_food != 'quit':
    Chinese_food = input(message)

    if Chinese_food != 'quit':
        print(Chinese_food)
