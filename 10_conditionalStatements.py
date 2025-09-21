# if-elif-else statements

# Example 1 using traffic light

light = "green"
if (light == "green"):
    print("Go")
elif(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("wait")
else:
    print("light is broken")

# Example 2 using marks 

marks = int(input("Enter your marks: "))

if (marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
elif(marks >= 60 and marks < 70):
    grade = "D"
else:
    grade = "F"

print ("your grade is :" , grade)

# nesting of if-else statements

num = int(input("Enter a number: "))
if (num >= 0):
    if(num == 0):
        print("number is zero")
    else:
        print("number is positive")
else:
    print("number is negative")