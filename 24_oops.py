# Define a student class
class student:
    college_name = "arihant"  # class attribute

    @staticmethod
    def new():
        print("this is a static method")

    # Constructor to set name and marks
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("hello")

    # Method to greet the student
    def welcome(self):
        print("hello", self.name)

# Create student objects and show info
s1 = student("karan", 84)
s1.welcome()
print(s1.name, s1.marks, s1.college_name)

s2 = student("ajay", 38)
s2.welcome()
print(s2.name, s2.marks, student.college_name)

class new :
    @staticmethod #decorater
    def new1():
        print("this is a statid method")

new.new1() 