players = ['charles', 'max', 'luis', 'michael', 'james']
print(players[:6])
print(players[4:])
print(players[-3:])
print(players[0:6:2])

print("Here is my first three players in my F1 team:")
for three_players in players[0:3]:
    print("\t",three_players.title())

message = "The first three items in the list are:"
print("\n" + message)
print(players[0:3])

print("\nThree items form the middle of the list are:")
print(players[1:4])

print("\nThe last three players in the list are:")
print(players[2:])