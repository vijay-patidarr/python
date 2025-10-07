# creating a file management system

import os

def create_file(filename):
    try:
      with open(filename , 'x') as f:
         print(f"file with '{filename}' created successfully !!")

    except FileExistsError :
       print("file with '{filename}' already exists")

    except Exception as e :
       print("An unknown error occur !")

def view_allFile():
   files = os.listdir()
   if not files :
       print(" No files found")
   else:
      for file in files:
         print(file) 

def delete_files(filename):
    try:
       os.remove(filename)
       print(f"'{filename}' is deleted successfully !")
   
    except FileExistsError :
       print("file with '{filename}' already exists")

    except Exception as e :
       print("An unknown error occur !")
       
def read_file(filename):
   try:
      with open(filename , "r") as f:
         content = f.read()
         print(f"Content inside the '{filename}' is \n {content}")
         
   except FileExistsError :
       print("file with '{filename}' already exists")

   except Exception as e :
       print("An unknown error occur !")
       
def edit_file(filename):
   try:
      with open(filename , "a") as f:
       content = input("Enter content to add in file '{filename}':")
       f.write(content + "\n ")
       print("Content added to '{filename}' successfully !")
   
   except FileExistsError :
       print("file with '{filename}' already exists")

   except Exception as e :
       print("An unknown error occur !")
      
      
def main():
   while True:
     print("WELCOME TO FILE MANAGEMENT APP !")
     print("select an option to continue")
     print("1.Create file")
     print("2. View all files")
     print("3.Delete file")
     print("4.Read file")
     print("5.Edit file")
     print("6.Exit File Manager")
     
     choice = input("enter the number of task you have to perform (1-6):")

     if choice == '1':
      filename = input("enter a filename to craete a file :")
      create_file(filename)
      
     elif choice == '2':
      view_allFile()
      
     elif choice == '3':
      filename = input("enter a filename to delete it :")
      delete_files(filename)
      
     elif choice == '4':
      filename = input("enter a filename to raad it :")
      read_file(filename)
      
     elif choice == '5':
      filename = input("enter a filename to edit it :")
      edit_file(filename)
   
     elif choice == '6':
      print("closing the app....")
      break
   
     else:
        print("invalid value !")
   
if __name__=="__main__":
   main()