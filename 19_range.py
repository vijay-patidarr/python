seq = range(5)

for i in seq :
    print(i)
else :
    print("end")

#  range(start?,stop,step?)

for i in range(1,10,2) :
    print(i)
else :
    print("end")    

for i in range(1,10) :
    print(i)
else :
    print("end")

# pass used to avoid error in empty loops

for i in range(10) :
    pass # it will do nothing and avoid error

print("end")