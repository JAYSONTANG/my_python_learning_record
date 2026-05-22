sandwich_orders = ['Chicken', 'pork', 'pastrami', 'beef', 'pastrami', 'rabbit']
finished_sandwiches = []

print("Sorry,Pastrami Sandwich have been sold out.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"I made your {sandwich_orders}. ")
    finished_sandwiches.append(sandwich)

print("\n--- All sandwiches have been made right now ---")
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich.title()} Sandwich")
