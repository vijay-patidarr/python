# Learning Dictionary Methods in Python

my_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}

print("Original dictionary:", my_dict)

# 1. get() method
print("\nUsing get():")
print("Value of key 'a':", my_dict.get("a"))
print("Value of key 'x' (not found):", my_dict.get("x", "Default Value"))

# 2. keys() method
print("\nUsing keys():")
print("Keys:", my_dict.keys())

# 3. values() method
print("\nUsing values():")
print("Values:", my_dict.values())

# 4. items() method
print("\nUsing items():")
print("Items (key-value pairs):", my_dict.items())

# 5. update() method
print("\nUsing update():")
my_dict.update({"d": 4, "a": 10})
print("After update:", my_dict)

# 6. pop() method
print("\nUsing pop():")
removed_value = my_dict.pop("b")
print("Removed value:", removed_value)
print("After pop:", my_dict)

# 7. popitem() method
print("\nUsing popitem():")
last_item = my_dict.popitem()
print("Removed last item:", last_item)
print("After popitem:", my_dict)

# 8. clear() method
print("\nUsing clear():")
my_dict.clear()
print("After clear:", my_dict)

print("\nEnd of dictionary methods example!")
