class car :
    def __init__(self , type ):
        self.type = type 

    color = "black" 
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stoped...")

class ToyotaCar (car):
    def __init__(self , name , type ):
        self.name = name 
        super().__init__(type)
        super().start()

car1 = ToyotaCar("fortuner","petrol")

print(car1.name)
print(car1.type)

class person:
    name = "unknown"

    def newname(self ,name ):
        person.name = name  # canges name on both places 
        # self.__class__.name = "vijay"
per1 = person()
per1.newname("vijay")
print(per1.name)
print(person.name)