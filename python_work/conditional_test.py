goat = "michael jordan"
print("Is goat == 'lebron james',I predict False.")
print(goat == 'lebron james')

print("\nIs goat != 'michael jordan'?I predict False.")
print(goat != 'michael jordan')

print("\nIs goat != 'lebron james'?I predict True.")
print(goat != 'lebron james')

print("\nIs goat == 'michael jordan'?I predict True.")
print(goat == "michael jordan")

goat = "Cristiano Ronaldo"
print("\nIs goat == 'lionel messi'?I predict True.")
print(goat == "lionel messi")

print("\nIs goat != 'cristiano ronaldo'?I predict False.")
print(goat.lower() == 'cristiano ronaldo')

numbers = [77,23,24]
print("\nIs 4 > 77?I predict False")
print(numbers[0] > 77)

print("\nIs 77 >= numbers[0]?I predict true.")
print(77 >= numbers[0])

lucky_number = 7
if lucky_number not in numbers:
    print("404 NOT FOUND.")

if lucky_number in numbers:
    print("lets go.")
