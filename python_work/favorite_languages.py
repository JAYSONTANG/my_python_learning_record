favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'javascirpt',
    }


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi,{name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()},I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please talk our poll!")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

poll_people = ['sarah', 'edward', 'jayson', 'bruce']

for people in poll_people:
    if people in favorite_languages.keys():
        print("Thanks for your polling!")
    else:
        print(f"{people.title()},would you like to join this poll?")


