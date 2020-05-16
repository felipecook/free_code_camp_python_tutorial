

name = input("What is your name? :")

print("Hello: " + name)


# this adds one list to another list
numbers = [1, 6, 8, 5, 4, 3]
friends = ["karen", "johnny", "peter", "john"]
friends.extend(numbers)
print(friends)


# this adds an item to the end of a list
friends = ["karen", "johnny", "peter", "john"]
friends.append("nate")
print(friends)


# this adds an item to the given index
friends = ["karen", "johnny", "peter", "john"]
friends.insert(1, "nate")
print(friends)


# removes an element from the list
friends = ["karen", "johnny", "peter", "john"]
friends.remove("john")
print(friends)


# removes all elements from a list
friends = ["karen", "johnny", "peter", "john"]
friends.clear()
print(friends)


# pops an element off a list, can be put into a value
friends = ["karen", "johnny", "peter", "john"]
friends.pop()
print(friends)


# tells you if an element is in the list
friends = ["karen", "johnny", "peter", "john"]
print(friends.index("peter"))


# tells you the number of times something is in a list
friends = ["karen", "johnny", "peter", "john", "john"]
print(friends.count("john"))


# this sorts the list in ascending order
numbers = [10, 6, 8, 5, 4, 3]
numbers.sort()
print(numbers)


# this reverses the list (can use with sort to sort and then reverse)
numbers = [10, 6, 8, 5, 4, 30]
numbers.reverse()
print(numbers)


# this copies one list to another list
numbers = [10, 6, 8, 5, 4, 30]
numbers_copy = numbers.copy()
print(numbers_copy)

