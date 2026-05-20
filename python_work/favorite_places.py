favorite_places = {
    'Jayson': ['London', 'Shandong'],
     'Bruce': ['Luoyang', 'Chengdu', 'Los Angeles'],
      'Catherine': ['Sydney', 'Seoul', 'Chamonix'],
        }

for name, place in favorite_places.items():
    print(f"\n{name}'s favorite places are:")
    for places in place:
        print(f"\t{places}")
