human ={'first_name': 'Jayson', 
        'last_name': 'Tang',
         'age': 23,
          'city': 'Beijing',
            }

for key, value in human.items():
    print(f"{key.replace('_',' ').title()}: {value}")
    