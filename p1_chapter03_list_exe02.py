numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
print(len(numbers))

#  3-8. Seeing the World: Think of at least five places in the world you’d like  
# to visit.
#  • Store the locations in a list. Make sure the list is not in alphabetical order.
citys = ["Madrid", "Bruxelas", "Berlin", "Curitiba", "Buenos Aires"]
#  • Print your list in its original order. Don’t worry about printing the list neatly; 
# just print it as a raw Python list.
print(citys)
#  • Use sorted() to print your list in alphabetical order without modifying the 
# actual list.
sorted(citys)
#  • Show that your list is still in its original order by printing it.
print(citys)
#  • Use sorted() to print your list in reverse-alphabetical order without chang
# ing the order of the original list.
print(citys.reverse())
#  • Show that your list is still in its original order by printing it again.
print(citys)
#  • Use sort() to change your list so it’s stored in alphabetical order. Print the 
# list to show that its order has been changed.
print(citys.sort())
