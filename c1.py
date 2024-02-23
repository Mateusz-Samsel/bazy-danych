import math
def silnia(n):
    s=1
    for i in range(1,n+1,1):
        s*=i
    return s
var1 = 2
var2 = 3
var1+=2
var3=var1
var1*=3
var4=var1/var2
print(var1, var2,var3, var4)
var4 /=2
print('var4= ', var4)


############## Tabliczka mnożenia
n=int(input("Podaj liczbę całkowitą: "))

gorna = "    "
linia=" 0    "

if n > 100:
    print("n is too large")
else:
    for i in range(1,n+1,1):
        gorna+=f"  {i}   "
    print(gorna)
    for k in range(0,n+1,1):
        for i in range(1,n+1,1):
            #if k<10:
            linia += f"{k*i}    "
        #    elif k<25:
         #       linia += f"{k * i}   "
          #  else:
           #     linia+= f"{k * i}  "
        print(linia)
        linia=f" {k+1}    "

############ Ułamek nieskracalany ###########
a1=int(input("Podaj liczbe a: "))
b1=int(input("Podaj liczbe b: "))
c1=math.gcd(a1,b1)
p=int(a1/c1)
q=int(b1/c1)
print(f"{p}/{q}")

def euler():
    ############## e1 ##########
    e=math.e
    o=int(input("Podaj n: "))
    e1=(1+(1/o))**o
    e2=0
    ############# e2 ##########
    for i in range(0,o,1):
        e2+=1/silnia(i)
    print(f"e1: {e1}; e2: {e2}; math.e: {math.e}")
    print(e1-math.e)
    print(e2-math.e)
    print(abs(e1 - math.e))
    print(abs(e2 - math.e))
euler()


def nwd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return print(f"Największy wspólny dzielnik to: {a}")
print(nwd(15,9))