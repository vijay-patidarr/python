# type conversion (automatic)

a = 3
b = 2.5
c = a + b  # Python automatically converts 'a' to float
print(c)   # Output: 5.5
print(type(c))  # Output: <class 'float'>

# type casting (manual)
x = 7
y = "4"
y_int = int(y)  # manually converting string to integer
result = x + y_int
print(result)   # Output: 11
print(type(y_int))  # Output: <class 'int'>