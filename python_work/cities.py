cities = {
    'Beijing': {
    'country': 'China',
     'population': 21800000,
      'fact': 'forbidden city',
      },
      'London': {
          'country': 'England',
          'population': 8900000,
          'fact': 'foggy city',
      },
      'Madrid': {
          'country': 'Spain',
          'population': 3300000,
          'fact': 'Real Madrid',
      },
      }

for city, info in cities.items():
    print(f"\nCity:{city}")
    print(f"\tCountry:{info['country']}")
    print(f"\tPopulation:{info['population']:,}")
    print(f"\tFact:{info['fact']}")
