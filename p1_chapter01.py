name = "ada"
full_name = "lovelace"
print(f"Hello, {name.title()} {full_name.title()} \n\tHow are you?")


x = "    matheus"
print(x.strip()) # rstrip => right and lstrip => left


site_url = "https://www.google.com"
clean_url = site_url.removeprefix('https://')
print(clean_url)