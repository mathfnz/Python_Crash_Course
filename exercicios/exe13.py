# %%
# Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.


fruits: dict = {
    "Maçã": 1.50,
    "Banana": 2.75,
    "Uva": 1.90,
    "Pera": 1.25,
    "Laranja": 0.65,
    "Limão": 1.25,
    "Goiaba": 2.15,
    "Abacaxi": 3.20,
    "Jaca": 5.80
}

fruit: str = input("Type you fruit: ").title()

for key, value in fruits.items():
    if key == fruit:
        print(f"{key}: R$ {value}")
if fruit != key:
    print("Type a valid fruit!")
        

