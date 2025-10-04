import os

with open("demo.txt", "r") as f:
    line1 = f.readline() # read the first line
    print(line1)
    line2 = f.readline() # read the second line
    print(line2)
    print(f.readline())

os.remove ("demo1.txt")