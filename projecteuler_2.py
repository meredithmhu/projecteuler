#Meredith Hu
#Project Euler - Even Fibonacci numbers
#2017-6-21

def fib(n):
    #returns a list of the fibonacci numbers with the last number being smaller than n
    fib=[1,1]
    cur = 0
    index=1
    while cur<n:
        cur=fib[index-1]+fib[index]
        if cur<n:
            fib.append(cur)
        index+=1
    return fib

def evenFib(L):
    #makes a new list composed of the even elements of the input, and sums the elements of the new list
    new=[]
    for n in L:
        if n%2==0:
            new.append(n)
    s=0
    for i in new:
        s+=i
    return s

print evenFib(fib(4000000))
