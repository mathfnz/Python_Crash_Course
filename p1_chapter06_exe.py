# %%
# 6-1. Person: Use a dictionary to store information about a person you know. 
# Store their first name, last name, age, and the city in which they live. You 
# should have keys such as first_name, last_name, age, and city. Print each piece  
# of information stored in your dictionary.

person: dict = {
    'first_name': 'cesar',
    'last_name': 'fernandes',
    'age': 63,
    'city': 'Sao Paulo'
}

for key in person:
    print(person[key])
# %%
# # 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
# # Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print 
# each person’s name and their favorite number. For even more fun, poll a few 
# friends and get some actual data for your program

person['favorite_number'] = 9
print(person)

# # %%
#  6-3. Glossary: A Python dictionary can be used to model an actual dictionary. 
# However, to avoid confusion, let’s call it a glossary.
#  • Think of five programming words you’ve learned about in the previous 
# chapters. Use these words as the keys in your glossary, and store their 
# meanings as values.
#  • Print each word and its meaning as neatly formatted output. You might 
# print the word followed by a colon and then its meaning, or print the word 
# on one line and then print its meaning indented on a second line. Use the 
# newline character (\n) to insert a blank line between each word-meaning 
# pair in your output.

glossary: dict[str, str] = {
    'name': 'nome',
    'years': 'anos',
    'favorite_number': 'numero favorito'
}

for key, value in glossary.items():
    print(f"{key} in portuguese means {value}")
    
# %%
favorite_cars: dict[str, str] = {
    'matheus': 'BMW',
    'kaina': 'Audi',
    'felipe': 'Honda'
}

for key, value in favorite_cars.items():
    print(f"{key} favorite car is: {value}")
    
for key in favorite_cars.keys():
    print(key)

for value in favorite_cars.values():
    print(value)

# %% 
# using sorted in a dictionary

for name in sorted(favorite_cars.keys()):
    print(f"{name.title()}, thank you!")