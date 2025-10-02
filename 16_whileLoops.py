# while loop
a = 1
while a <= 10 :
    print("hello" , a)
    a += 1

b = 10 
while b >= 1 :
    print("hello" , b)
    b -= 1 

# print number from 1 to hundred

# c = 100 
# while c >= 1 :
#     print(c)
#     c = c - 1        

# num = int(input("enter your number and get the table of that number :"))
# i = 1

# while i <= 10 :
#     print (i*num)
#     i += 1

# list1 = [1,5,2,6,8,65,2,]
# i = 0 
# while i <= len(list1):
#     print(list1[i])
#     i+= 1

num = (1,2,3,4,5,6,7,8,9)

x = 5

i = 0 
while i < len(num) :
    if (num[i] == x) :
     print("number found at " , i)
    else :
     print("finding...")
    i += 1
print ("search completed ")