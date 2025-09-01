# %%
alien_0: dict = {
    'color': 'green',
    'points': 5
}

# for access a value: dict[key]
print(alien_0['points'])

new_points = alien_0['points']
print(f"{new_points}")

# add key-value: dict[key] = value
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# modify a dict
alien_0['color'] = 'black and white'
print(alien_0)

# %%
alien_1: dict = {
    'x_position': 0,
    'y_position': 25,
    'speed': 'medium'
}
print(f'Original position: {alien_0['x_position']}')

if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
    
alien_1['x_position'] += x_increment
print(f"new position: {alien_1['x_position']}")

# %%
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

f_language = favorite_languages['phil'].title()
print(f_language)

ide_favorite = favorite_languages.get('matheus', 'no name assigned')
print(ide_favorite)

# %%
# 6.1
favorite_person: dict = {
    'first_name': 'Matheus',
    'last_name': 'Fernandes',
    'city': 'Sao Paulo'
}
print(favorite_person)
favorite_person['favorite_number'] = 20
print(favorite_person)

# %%
# 6.2
name_numbers: dict = {
    'Matheus': 20,
    'Amanda': 19,
    'Marina': 22
}
for name, number in name_numbers.items():
    print(name, number)
    
# %%
user_0: dict = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
# %%
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name)

for language in favorite_languages.values():
    print(language)
print("------")
for name, language in favorite_languages.items():
    print(f"name: {name}, favorite language is {language}")
    
favorite_languages['matheus'] = 'python3'
print(favorite_languages)
    
# %%

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
print("----------")
#chave da lista, chave do dicionario dentro da lista
print(aliens[0]['points'])

# %%
aliens: list = []

# make 30 aliens
for alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
print(aliens)
print("----")

for alien in aliens[:5]:
    print(alien)