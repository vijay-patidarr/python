# recursion 
# A function that calls itself is called a recursive function.

def  numb(n):
    if n == 0 :
        return
    print(n)
    numb(n-1)


numb(5)