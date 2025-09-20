# input function example

# taking name as input from user (input is always string)
name = input("Enter your name: ")
print("Welcome,", name)
print("Type of name:", type(name))  # <class 'str'>

# taking age as input and converting to integer
age = int(input("Enter your age: "))
print("Your age is", age)
print("Type of age:", type(age))    # <class 'int'>