prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"\nHello,{name}!")

age = input("How old are you? ")
age = int(age)

if age >= 18:
    print(f"Your age is {age}.")
