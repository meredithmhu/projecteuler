#Meredith Hu
#Project Euler - Multiples of 3 and 5
#2017-6-20

def mults():
    s = 0
    threes=0
    while threes <999:
        threes+=3
        s+=threes
    fives=0
    while fives<995:
        fives+=5
        if fives%3==0:
            fives+=5
        s+=fives
    return s

print mults()
