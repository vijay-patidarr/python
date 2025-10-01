# Learning About Dictionaries in Python

# Creating a dictionary
student = {
    "name": "John",
    "age": 20,
    "course": "Computer Science"
}

print("Original dictionary:", student)

# Accessing values using keys
print("\nAccessing values:")
print("Name:", student["name"])
print("Age:", student["age"])

# Adding a new key-value pair
student["grade"] = "A"
print("\nAfter adding a new key-value pair:")
print(student)

# Updating a value
student["age"] = 21
print("\nAfter updating age:")
print(student)

# Deleting a key-value pair
del student["course"]
print("\nAfter deleting 'course':")
print(student)

# Looping through dictionary
print("\nLooping through dictionary:")
for key in student:
    print(key, ":", student[key])

print("\nEnd of basic dictionary example!")
