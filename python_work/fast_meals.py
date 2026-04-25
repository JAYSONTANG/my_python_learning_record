fast_meals = ['mc donald', 'kfc', 'dustin']
for fast_meal in fast_meals:
    print(f"I like {fast_meal.upper()}\n")

print("I really love fast food!")

friend_fast_meals = fast_meals[:]
fast_meals.append("in n out")
friend_fast_meals.append("pizza hut")

print("\nmy favorite fast meals are:".capitalize())
for my_meals in fast_meals[0:]:
    print(my_meals.upper())

print("\nmy friend favorite fast meals are:".capitalize())
for friend_meals in friend_fast_meals[0:]:
    print(friend_meals.upper())