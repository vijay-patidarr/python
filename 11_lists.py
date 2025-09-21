# lists data type in Python

marks = [90.5 , 85.0, 78.5, 92.0]  
print(marks)
print(type(marks))  # prints the type of the variable 'marks'
print(marks[0])  # prints the first element of the list
print(len(marks))  # prints the number of elements in the list

student = ["vijay", 21, True, 5.9]  # list with mixed data types
print(student)

# list are mutable
student[0] = "ajay"
print(student)

# list slicing
print(marks[0:3])  # prints elements from index 0 to 1
# negetive indexing
print(marks[-1])  # prints the last element of the list