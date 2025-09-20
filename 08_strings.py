# String basics in Python

# simple string
name = "vijay"
print(name)

# string concatenation
full_name = name + " " + "patidar"
print(full_name)

# string length
print(len(full_name))  # prints the number of characters in the string

# # indexing: accessing individual characters in a string using their position (index)
print(full_name[0])    # prints first character

# slicing: extracting a substring from a string using a range of indices
print(full_name[0:5])  # prints 'vijay'
print(full_name[6:])   # prints 'patidar'
print(full_name[:5])   # prints 'vijay' 
print(full_name[:])    # prints the whole string

# escape characters
print("He said, \"Hello!\"")  # prints double quotes inside string
print('It\'s Python!')        # prints single quote inside string

# negetive index
str1 = "Hello"
print(str1[-5 : -1])