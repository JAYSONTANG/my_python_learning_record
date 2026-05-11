dictionary = {'variable': 'stock',
              'string': 'words',
              'method': 'magic',
              'for_loop': 'loop something',
              'if_statement':'calculate all the odds',
                }

for key, value in dictionary.items():
    print(f"{key.replace('_',' ').title()}:\n{value}")
