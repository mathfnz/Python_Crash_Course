# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, 
# inclusive.

for n in range(1, 21):
    print(n)
    
# 4-4. One Million: Make a list of the numbers from one to one million, and then 
# use a for loop to print the numbers. (If the output is taking too long, stop it by 
# pressing CTRL-C or by closing the output window.)

# for m in range(1, 1000001):
#     print(m)
    
# 4-5. Summing a Million: Make a list of the numbers from one to one million, and 
# then use min() and max() to make sure your list actually starts at one and ends 
# at one million. Also, use the sum() function to see how quickly Python can add 
# a million numbers.
one: list[int] = []

for y in range(1, 100001):
    one.append(y)
print(max(one))
print(min(one))
print(sum(one))    