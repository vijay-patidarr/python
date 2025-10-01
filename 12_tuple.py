# Learning About Tuples in Python

# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)
print("Original tuple:", my_tuple)

# Tuples can also contain different data types
mixed_tuple = (1, "apple", 3.14, True)
print("Mixed tuple:", mixed_tuple)

# Accessing elements in a tuple using index
print("\nAccessing elements:")
print("First element:", my_tuple[0])
print("Third element:", my_tuple[2])

# Tuples are immutable, so this will give an error if we try to change a value
# Uncomment the next line to see the error
# my_tuple[1] = 100

# Tuple slicing
print("\nSlicing tuples:")
print("Elements from index 1 to 3:", my_tuple[1:4])

# Tuple methods
numbers = (1, 2, 2, 3, 4, 2, 5)

# 1. count() - counts how many times an item appears
print("\nUsing count() method:")
print("How many times 2 appears:", numbers.count(2))

# 2. index() - returns the index of the first occurrence of an item
print("\nUsing index() method:")
print("Index of 3:", numbers.index(3))

# Using len() to find the length of a tuple
print("\nLength of my_tuple:", len(my_tuple))

# Looping through a tuple
print("\nLooping through tuple values:")
for item in my_tuple:
    print(item)

# Nesting tuples
nested_tuple = (("a", "b", "c"), (1, 2, 3))
print("\nNested tuple:", nested_tuple)
print("Accessing nested value:", nested_tuple[1][2])

# Converting a list to a tuple
my_list = [100, 200, 300]
converted_tuple = tuple(my_list)
print("\nList converted to tuple:", converted_tuple)

print("\nEnd of tuple learning example!")
