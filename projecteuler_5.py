#Meredith Hu
#Project Euler - Smallest multiple
#2018-9-10

def mult():
    num = 1
    divisor = 1
    while divisor < 16:
        isDiv = True
        for x in range(divisor):
            if num%(x+1)!=0:
                isDiv=False
        if isDiv==True:
            divisor+=1
        #print divisor
        num +=1
    return num-1

print mult()
print range(2)
