#%%
hi = "Hello word!"
type(hi)
# %% 2.1
name: str = "Olá, Matheus"
print(name)
# %% 2.2
hi: str = "Olá, Matheus"
print(hi)
hi: str = "matheus"
print(hi)
# %%
print(hi.upper())
# %%
print(f"Hello, {hi.title()}")
# %%
espaco = "   Matheus Silva Fernandes.   "
print(espaco.strip())

# %%
google = "https://www.google.com"
print(google.removeprefix("https://"))
# %%
# 2.3
name: str = "Matheus"
print(f"Hello, {name}. Would you like to learn some Python today?")
# %% 
# 2.4
print(f"{name.lower()}\n{name.upper()}\n{name.title()}")
# %% 
# 2.5
name: str = "Albert Einstein"
quote: str = "A person who never made a mistake never tried anything new."
print(f"{name}, once said: {quote}")
# %%
# 2.7
name = "        matheus.           "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# %%
# 2.8
filename = "python_notes.txt"
print(filename.removesuffix(".txt"))
# %%
run_1000: list = [x for x in range(1, 100_000)]
print(run_1000)
# %%
# 2.9
print(4+4)
print(16-8)
print(2*4)
print(64/8)
# %%
# 2.10
favorite_number = 9
print(favorite_number)
type(favorite_number)
# %%
# 2.11
# I'm using #2.11 as a track markers exercises
import this
# %% 
# 3.1
names: list = ['Matheus', 'Felipe', 'Kaina']
print(names[0].upper())
print(names[1].upper())
print(names[2].upper())
# %%
# 3.2
all_names = [name.upper() for name in names]
print(f"Using a list with list comprehension {all_names}")

# %%
# 3.3
favorite_transportations : list = ['subway', 'public transport', 'bus', 'bicycle']
print(favorite_transportations)
all_transports: list = [transport.title() for transport in favorite_transportations]
print(f"using list comprehension: {all_transports}")
favorite_transportations[-1] = 'car'
print(favorite_transportations)
favorite = favorite_transportations.pop(0)
print(favorite)
print(favorite_transportations)
# %%
numbers: list[float] = [3.4, 99.5, 0.2, 22.1, 89]
soma = sum(numbers)
print(soma)
media = sum(numbers) / len(numbers)
print(f"{media:.2f}")
numbers.insert(0,3)
print(numbers)
del numbers[0]
print(numbers)

# %%
# 3.4
guests: list[str] = ['Michelangelo', 'Iolanda', 'Kuhn']
invite_guests = [print(f"Hi {guest}, do you want to dinner?") for guest in guests]
# %%
# 3.5
guests: list[str] = ['Michelangelo', 'Iolanda', 'Kuhn']

cancel_invite = [print(f"Im so sorry {guest}") for guest in guests if guest == 'Michelangelo']
guests.pop(0)
still_invite = [print(f"But you guys still on the list, right?! {guest}") for guest in guests]

# %%
# 3.6
bigger_table_list: list = [print(f"{guest} guess what! I just find a bigger table!") for guest in guests]
guests.insert(0, 'Sócrates')
print(guests)