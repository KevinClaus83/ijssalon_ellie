i=3
def mijn_functie_1():
    list = [2,4,10,12]
    global i
    if i in list:
        print(i**2)
    else:
        print(i)
    
mijn_functie_1()