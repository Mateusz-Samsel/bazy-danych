import re
def pkt1(napis):
    wynik=""
    for i in range(len(napis)):
        if i%2==0:
            wynik+=napis[i]
    return print(wynik)
napis="Zbłąkany kot Kasi wędrował po łąkach"
pkt1(napis)

##############################################

def pkt2(napis):
    n=int(input("Podaj ile znakow od konca mam podac: "))
    return print(napis[-n:])
pkt2(napis)

##############################################

def pkt3():
    wynik=""
    napis1=input("Podaj dowolny ciąg znaków: ")
    for i in range(len(napis1)):
        wynik+=napis1[-(i+1)]
    return print(wynik)
pkt3()

##############################################

def pkt4(napis):
    wynik=""
    napis.strip(" ")
    for i in range(len(napis)):
        wynik+=napis[-(i+1)]
    if wynik==napis:
        return print("Jest to palindrom")
    else:
        return print("To nie jest palindrom")
pkt4("kamilślimak")

##############################################

def pkt5(napis1,napis2):
    if len(napis1)>len(napis2):
        return print("Zawartość pierwszej zmiennej jest dłuższa")
    elif len(napis1)<len(napis2):
        return print("Zawartość drugiej zmiennej jest dłuższa")
    if len(napis1)==len(napis2):
        return print("Zawartość obu stringów są równe długością.")
pkt5("Ala ma kota","Kasia nie ma kota")

##############################################

def pkt6(imie,dataUr):
    return print(f"My name is {imie}. My date of birth is {dataUr}".format(imie,dataUr))
pkt6("Mateusz","2003-10-30")

##############################################

def pkt7():
    suma=0
    napis="W Roku Pańskim 1345, władca Henryk 12, na rzecz swoich 143209 poddanych uchwalił dekret o 20 procentowej zniżce podatków"
    wynik = re.findall(r'\d+', napis)
    wynik = list(map(int, wynik))
    print(wynik,int(wynik[2]))
    for i in range(len(wynik)):
        suma+=int(wynik[i])
    return print(f"Suma: {suma}")
pkt7()