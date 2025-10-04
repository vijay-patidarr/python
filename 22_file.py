# reading a file

f = open("demo.txt", "r")
# data = f.read() # read the entire file
# data = f.read(10) # read the first 10 characters
# print(data)
# print(type(data))

line1 = f.readline() # read the first line
print(line1)
line2 = f.readline() # read the second line
print(line2)
print(f.readline())
f.close()

# writing to a file

f = open("demo.txt", "a") # append mode adds data to the end of the file 
# f = open("demo.txt", "w") # write mode overwrites the entire file
f.write(" this is a  new line ")
f.close()

f = open("demo1.txt", "a")
f.write(" this is a  new file ")
f.write(" this is a  new line ")
f.close()