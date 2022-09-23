import heapq
import sys
import math

def lesFraFil():
    input = []
    heapq.heapify(input)

    for line in sys.stdin:
        heapq.heappush(input, int(line))
    
    # print(input)
    balance(input)

def balance(heap1):
    if len(heap1) == 0: return
    mid = math.floor(len(heap1)/2)

    heap2 = [] 
    heapq.heapify(heap2)
    for i in range(mid):
        heapq.heappush(heap2, heapq.heappop(heap1))
    
    print(heapq.heappop(heap1))
    balance(heap1)
    balance(heap2)


lesFraFil()