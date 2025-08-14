
def soma(n1: float, n2: float) -> float:
    resultado = n1 + n2
    return resultado

def avg(n1: float, n2: float) -> float:
    avg_result = soma(n1, n2) / 2
    return avg_result

number1 = float(input("Type the first number: "))
number2 = float(input("Type the second number: "))

sum = soma(n1 = number1, n2= number2)
print(f"{number1} + {number2} = {sum}")

avg_result = avg(n1 = number1, n2= number2)
print(f"The avarage of {number1} and {number2} is {avg_result}")


