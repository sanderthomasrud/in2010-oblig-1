import sys

path = []

def lesFraFil():
    hovedArray = []

    katt = None
    for linje in sys.stdin:
        ordListe = linje.split()

        if katt is None: katt = linje
        elif int(ordListe[0]) == -1:
            finnVei(int(katt), hovedArray)
        else:
            hovedArray.append(ordListe)
        

def finnVei(posKatt, arrays):
    path.append(posKatt)

    for array in arrays:
        for element in array:
            if int(element) == int(posKatt) and int(element) != int(array[0]):
                finnVei(array[0], arrays)
    
    return


lesFraFil()
print(*path)