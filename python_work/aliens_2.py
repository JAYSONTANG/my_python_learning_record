alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'purple', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# a blank list of aliens
aliens = []

# 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'purple'
        alien['speed'] = 'high'
        alien['points'] = 100

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens created
print(f"Total number of aliens: {len(aliens)}")
