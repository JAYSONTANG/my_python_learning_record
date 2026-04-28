requested_topping = 'mushroom' 

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

requested_toppings =['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("adding extra cheese.")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry,we are out of green peppers right now.")
    else:
        print(f"\nAdding {requested_topping}")

print("\n Finished making your pizza!")

requested_toppings =[]

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
else:
    print("Are you sure you wanna a plain pizza?")

avaliable_toppings = ('mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese')
requested_toppings = ['pepperoni', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in avaliable_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"We don't have {requested_topping}")

print("\nFinished making your pizza!")