class car :
    color = "black" 
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stoped...")

class ToyotaCar (car):
    def __init__(self , name , sunroof ):
        self.name = name 
        self.sunroof = sunroof

class Fortuner (ToyotaCar):
    def __init__(self, type):
        self.type = type 


car1 = ToyotaCar("fortuner" , "yes") 
car2 = ToyotaCar("prius" , "No")
fortuner1 = Fortuner("Petrol")
print(car1.name)
print(car1.start())
print(car2.color)
print(fortuner1.color)

# multiple inheritance

class A:
     varA = "this is variable a"

class B:
    varB = "this is variable b"

class C(A, B):
    varC = "This is variable c"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)
