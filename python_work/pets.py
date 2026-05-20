pet_1 = {'type': 'dog',
         'owner': 'Bruce',
         'name': 'Paul',
         }

pet_2 = {'type': 'cat',
         'owner': 'Jayson',
         'name': 'Luka',
         }

pet_3 = {'type': 'chicken',
         'owner': 'Deng',
         'name': 'Kunxin',
         }

pet = [pet_1, pet_2, pet_3]

for pets in pet:
    print(f"\nType: {pets['type']}")
    print(f"{pets['owner']}")
    print(f"{pets['name']}")