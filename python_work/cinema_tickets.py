asking = "We have different ticket fee taking policy based on your age."
asking += "\nPlease tell me your age: "
asking += "When you enter your age, please enter 'quit' to end."

while True:
    age = input(asking)
    if age == 'quit':
        print("Goodbye,have a nice day.")
        break
    
    age = int(age)
   
    if age <= 3:
        print(f"\nYour age is {age}. You can watch for free!")
    elif 3< age < 12:
        print(f"\nYour ticket costs 10 dollars.")
    else:
        print("Your ticket costs 15 dollars.")
    

