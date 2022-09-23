import sys
import math

def lesFraFil():
    input = []

    for line in sys.stdin:
        input.append(line)

    balance(input)

def balance(liste):
    if len(liste) == 0: return
    
    mid = math.floor(len(liste)/2)

    print(liste[mid])
 
    balance(liste[mid + 1:])
    balance(liste[:mid])


lesFraFil()