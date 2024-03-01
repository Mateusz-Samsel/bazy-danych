import math

a = 10
x = 120
y = 10.2
n = 50
napis= "Ala miałaby kota, ale go zgubiła."
print(round(a), math.ceil(a), math.floor(a))

#
#                Zadanie 1
###############################################
if isinstance(x, int) & isinstance(y, int):
    print(x % y)
else:
    print(math.fmod(x, y))
###############################################
#
#                 Zadanie 2
################################################
for k in range(n):
    if k > 1:
        print(f"Podstawa log {k} = {math.log(a, k)}")
    k += 1
###############################################
#
#                 Zadanie 3
################################################
print(math.exp(a), math.e ** a, math.pow(math.e, a))

print(napis[12],len(napis))