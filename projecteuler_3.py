#Meredith Hu
#Project Euler - Largest prime factor
#2017-6-21

def isPrime(L,num):
    #checks if a number is prime (not for all numbers ever though)
    for n in L:
        if num%n==0:
            return False
    return True

def primeGen(n):
    #generates list with last element smaller than n
    L=[2]
    last=L[-1]
    num=L[-1]+1
    while num<n:
        if isPrime(L,num):
            L.append(num)
        num+=1
    return L

def factorChecker(n):
    #given a number, n, finds the largest prime number factor of n
    thelist=primeGen(n**0.5)
    new=[]
    for i in thelist:
        if n%i==0:
            new.append(i)
    return max(new)

print factorChecker(600851475143)
