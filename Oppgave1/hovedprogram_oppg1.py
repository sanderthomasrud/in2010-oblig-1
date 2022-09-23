import sys
from binaersoketre import *


sett1 = BinaerSokeTre()
 
for linje in sys.stdin:
    ordListe = linje.split()
    if "contains" in linje:
        if (sett1.contains(sett1.root, ordListe[1])) is None:
            print(False)
        else:
            print(True)

    # elif "insert" in linje:
    #     if not sett1.contains(sett1.root, ordListe[1]):
    #         sett1.insert(sett1.root,ordListe[1])
    #         sett1.leggTil()

    elif "insert" in linje:
        if not (sett1.contains(sett1.root, ordListe[1])):
            sett1.insert(sett1.root, ordListe[1])

    elif "remove" in linje:
        if sett1.contains(sett1.root,ordListe[1]):
            sett1.remove(sett1.root,ordListe[1])
            sett1.trekkFra()

    elif "size" in linje:
        print(sett1.size())



