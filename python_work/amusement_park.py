age = 12
if age < 4:
    print("Your admission cost is 0 yuan.")
elif age <= 18:
    print("Your admission cost is 18 yuan.")
else:
    print("Your admission cost is 40 yuan.")
    
age = 17
if age < 4:
    price = 0
elif age < 18:
    price = 18
else:
    price = 40

print(f"\nYour admission cost is {price} yuan.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 18
elif age < 65:
    price = 40
elif age >= 65:
    price = 0

print(f"\nYour admission cost is {price} yuan.")