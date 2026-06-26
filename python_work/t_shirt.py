def make_shirt(size, text='I love Python'):
    """show the size and word on the shirt."""
    print(f"The size of the shirt is {size}.")
    print(f"we should print {text} on the shirt.\n")

make_shirt('L')
make_shirt('M')
make_shirt('XL', text='Marxist')

def describe_city(city, nation='China'):
    """show the city and the nation it belongs."""
    print(f"{city.title()} is in {nation.title()}.\n")

describe_city(city='beijing')
describe_city(city='shanghai')
describe_city(city='berlin', nation='deutschland')