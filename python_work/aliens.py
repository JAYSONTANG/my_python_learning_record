alien_0 = {'color': 'green','points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"you just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0) 

alien_0 = {'color': 'green'}
print(f"The alien was {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']} right now.")

alien_0 = {'x_position': 0,'y_position': 25, 'speed': 'highest'}
print(f"Original position:{alien_0['x_position']}")

# move the alien at right
# make sure how far the alien moves based on the speed right now 
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# new position = old position + moved distance
alien_0['x_position'] += x_increment

print(f"New position: {alien_0['x_position']}")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)