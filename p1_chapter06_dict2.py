# %%

favorite_languages: dict[str, str] = {
    'jen': 'python',
    'matheus': 'c',
    'ana': 'rust',
    'antonio': 'python'
}
print(favorite_languages)
language = favorite_languages['matheus'].title()
print(f"Matheus favorite language:  {language}")

# %%
# using get to avoid error if dont have the key
alien: dict = {
    'color': 'green',
    'x_position': 0
}

point_value = alien.get('points', 'No point value assigned.')
print(point_value)