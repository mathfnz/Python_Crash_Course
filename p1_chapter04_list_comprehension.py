# combines the for loop and the creation of new elements into one line, and automatically appends each new element

# numbers = []
# for number in range(1, 11):
#     numbers.append(number**2)
# print(numbers)

# 1 -> set the name of the list
# 2 -> set the equation that I want insinde 
# 3 -> for loop
numbers = [value**2 for value in range(1, 11)]
print(numbers)