# %%
def function (x):
    return print(1 + x)

# %%
def soma (n1: int, n2: int) -> int:
    """
  Esta função calcula a soma de dois números inteiros e retorna um inteiro.  
  :param n1: O primeiro número inteiro.
  :param n2: O segundo número inteiro.
  :return: A soma de n1 e n2.
  """   
    result = n1 + n2
    return result

calculo = soma(n1= 5, n2= 6)
print(calculo)


# %%
def mult (n1: float, n2: float) -> float:
    """
    Esta funcao calcula a multiplicao de dois floats e return um float
    
    :param n1: float
    
    :param n2: float
    
    :return: n1 * n2 
    """
    result = n1 * n2
    return result

number1 = 66
number2 = 77
calculo_mult = mult(n1 = number1, n2 = number2)
print(f"{number1} * {number2} = {calculo_mult}")

# %%
def bom_dia():
    print("Bom dia!")
    return

bomdia = bom_dia()

# %%

def odd_even(value: int) -> str:
    """
    This function shows if the number is Even or Odd
    
    :param value: int
    
    :return: value % 2 == 0 print even else is odd
    """
    if value % 2 == 0:
        print("Even")
    else:
        print("Odd")
    return
        
number = 2
odd_even(value = number)