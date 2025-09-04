# def xx (parameters):
#  xx(arguments)
# %%
# 8.1
def display_message():
    '''print what I'm currently learning'''
    print("I'm learning about functions")

display_message()
# %%
# 8.2
def favorite_book(title: str):
    '''print my favorite book'''
    f_book = print(title)

favorite_book('One of my favorite books are LoR')
# %%
def describe_pet(pet_animal: str, pet_name: str):
    '''print my favorite animal'''
    print(f"If I had a {pet_animal}, I would name it {pet_name}.")
                
describe_pet(pet_animal='cat', pet_name='Sauron')
                #parametro=argumento, paramentro=arguemtno
# %%
# 8.3
def make_shirt(size: int, message: str):
    '''function to print a t-shirt'''
    print(f"My size is {size} and I would like a message as {message}")
make_shirt(size=10, message="I love WoW")
# %%
def get_formatted_name_with_types(first_name: str, last_name: str) -> str:
    '''Return a full name, neatly formated'''
    full_name = (f"{first_name} {last_name}")
    return full_name.title()

musician = get_formatted_name_with_types(first_name='jimi', last_name='hendrix')
print(musician)

#%%
def build_person(first_name: str, second_name: str) -> dict[str, str]:
    """Return a dicitionary of information about a person"""
    person: dict[str, str] = {
        'first': first_name,
        'second': second_name
    }
    return person

musician = build_person("jimi", "hendrix")
print(musician)
# %%
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
# %%
# 8.6
