# creating a contact manager app
contacts = {} 
while True:
    
 print("WELCOME TO CONTACT APP")
 print("1 - NEW CONTACT")
 print("2 - VIEW CONTACT")
 print("3 - UPDATE CONTACT")
 print("4 - DELETE CONTACT")
 print("5 - SEARCH CONTACT")
 print("6 - COUNT CONTACT")
 print("7 - EXIT THE APP ")
 
 choice = input("enter a number to select the task (0-7) ; ")
 
 if choice == "1":
     name = input("enter a name to create a contact: ")
     if name in contacts:
         print("Contact already available")
     else:
         number = input("enter mobile number : ")
         age = int(input("enter your age : "))
         contacts[name] = {'mobile_number' : number , 'age' : age }
         print(f"contact named '{name}' is created successfully!")
         
 elif choice == "2":
     name = input("Enter name of contact you want to see :")
     if name in contacts:
          contact = contacts[name]
          print(f"contact details of '{name}' : '{contact}'")
     else:
         print("No contact details found!")
         
 elif choice == "3":
     name = input("enter a name to update a contact : ")
     if name in contacts:
         updated_number = input("enter mobile number : ")
         updated_age = int(input("enter your age : "))
         contacts[name] = {'mobile_number' : updated_number , 'age' : updated_age }
         print(f"contact from the name '{name}' is updated successfully!")
     else:
         print("No contact details found")
         
 elif choice == "4":
     name = input("input contact name you want to delete :")
     if name in contacts:
         del contacts[name]
         print("contact details deleted successfully!")
         
     else :
         print("No contact found from this name")
         
 elif choice == "5" :
     name = input("Search the contact :")
     if name in contacts:
         print(f"Contact found : '{contacts[name]}'")
     else :
         print(f"No contact found from '{name}'")
         
 elif choice == "6":
     print(f"total no. of contact in list : '{len(contacts)}'")
     
 elif choice == "7":
     print("Exiting the program...")
     break
 
 elif choice == '8':
     print(contacts)
     
 else:
     print("INVAILID INPUT !!")