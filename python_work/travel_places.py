responses = {}

active = True

while active:
    name = input("\nWhat is your name? ")
    response = input("\nIf You could visit one place in the world, " \
    "where wuould you go?")

    responses[name] = response

    repeat = input("Would you like to take someone? (Yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, place in responses:
    print(f"{name.title()} would like to go {place.title()}")