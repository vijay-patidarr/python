# sets 
# sets are used to store multiple items in a single variable.
# sets are unordered, unchangeable*, and do not allow duplicate values. 

set1 = {1,2,3,4,4, "hello","world",7} # duplicate values will be ignored
print(type(set1))
print(set1)
print(len(set1)) # returns the number of elements in the set

collection = {} # this will create an empty dictionary not a set
print(type(collection))
empty_set = set() # this will create an empty set
print(type(empty_set))

# set methods
set1.add(5) # adds an element to the set mutating the set
print("After add:", set1)

set1.remove(2) # removes an element from the set mutating the set, raises KeyError if the element is not found

# set is mutable but does not support item assignment

# set methods 

collection1 = {1,2,3,4}

collection1.add(5) # adds an element to the set mutating the set
collection1.add(5) # adding duplicate value will be ignored
collection1.add("hello")
collection1.add((1,2)) # adding a tuple is allowed as it is immutable
print("After add:", collection1)

collection1.remove(2) # removes an element from the set mutating the set, raises KeyError if the element is not found
print("After remove:", collection1)

collection1.clear() # removes all elements from the set mutating the set
print("After clear:", collection1)

collection2 = {1,2,3,4,4,5,6,7,8,9, "hello" , }

print(collection2.pop()) # removes and returns an arbitrary element from the set mutating the set, raises KeyError if the set is empty

collection3 = collection1.union(collection2) # returns a new set with all elements from both sets
print("After union:", collection3)

setA = {1,2,3,4,5}
setB = {4,5,6,7,8}  
setC = setA.intersection(setB) # returns a new set with elements that are common to both sets
print("After intersection:", setC)
