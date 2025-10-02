# break and continue 

num = [1 , 2 , 3 , 4 , 5 , 6 , 55 , 1, 3 , 8  ]
i = 55 
x = 0 
while x < len(num) :
    if (num[x] == i) :
        print("we found the number at" , x )
        break # it will break the loop if the condition is satisfied
    else :
        print("finding...")
    x += 1  

# continue statement

i = 0 

while i <= 5 :
    if i == 3 :
        i +=1
        continue # it will skip the current iteration if the condition is satisfied
    print(i)
    i +=1