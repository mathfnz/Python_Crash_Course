names = ['matheus', 'leticia', 'ligia', 'ana']

print(f"Bem vindo, {names[2].title()}")
names[0] = "fabricio" # alterei o matheus para fabricio
print(names)

del names[-1]
print(names)
popped_names = names.pop() # posso usar um numero de index que quiser
print(popped_names)
print(names)
names.append('Ligia')
print(names)