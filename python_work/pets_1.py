def describe_pet(pet_name,animal_type='cat'):
    """show the information of pets"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} name is {pet_name.title()}.")

describe_pet('abi')

