class student:
    
    def __init__(self, name):
     self.name = name 

s1 = student("karan")
# print(s1.name)
del s1.name  # delete the s1 object 

class account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # private variable

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = account("1234", "abcd")

print(acc1.acc_no)       # prints: 1234
acc1.reset_pass()        # prints: abcd

class Person:
     name = "anonymous"
     def _hello(self):
      print("hello person!")
    
     def welcome (self):
        self._hello()


p1 = Person()
print(p1.welcome())