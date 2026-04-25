my_foods = ['pizza','hamburger','fried rice']
friend_foods = my_foods[:]

my_foods.append("beijing duck")
friend_foods.append("cake")

print("my favorite foods are:".capitalize())
for my_food in my_foods[:]:
    print(my_food.title())

print("\nmy friend favorite foods are:".capitalize())
for friend_food in friend_foods[:]:
    print(friend_food.title())
