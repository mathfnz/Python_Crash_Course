# %%
alien: dict = {
    'color': 'green',
    'points': 5
}

new_points = alien['points']
print(f"You won {alien['points']} points!")
print(alien)

# %%
alien['x_position'] = 0
alien['y_position'] = 25
print(alien)

# %%
# add data into a empty dictionary
alien: dict = {
    
}
print(alien)
alien['color'] = 'blue'
alien['points'] = 10
print(alien)

# %%
# modify a dictionary value

alien['color'] = "red"
alien['x_position'] = 0
alien['y_position'] = 25
print(alien)
print(f"Now the color is: {alien['color']}")

alien['speed'] = 'fast'
print(alien)

# Move alien to the right - determine how fast the alien can move based on its current speed

if alien['speed'] == "slow":
    x_increment = 1
elif alien['speed'] == "medium":
    x_increment = 2
else:
    #this must be fast alien
    x_increment = 3

alien['x_position'] = x_increment + alien['x_position']

print(f"New position: {alien['x_position']}")

# %%
# Delet a key-value

del alien['y_position']
print(alien)
