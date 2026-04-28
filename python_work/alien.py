alien_color = 'green'
if 'green' in alien_color:
    print("Congrats,You get 5 points!")
if 'blue' in alien_color:
    print()

alien_color = 'yellow'
if 'green' in alien_color:
    print("\nYou just get 5 points!")
else:
    print("\nYou just get 10 points!")
    
alien_color = 'yellow'
if 'green' not in alien_color:
    print("\nYou just get 10 points!")
else:
    print("\nYou just get 5 points!")

if 'green' in alien_color:
    print("You just get 5 points!")
elif 'yellow' in alien_color:
    print("\nYou just get 10 points!")
else:
    print("You just get 15 points!")
