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

def balance(heap):
    if len(heap) == 1:
        print(heapq.heappop(heap))
        return

    print(heap)
    lengde = len(heap)
    mid = math.floor(lengde/2)
    print(heap(mid))

    balance(heapq.heapify(heap[mid+1:]))
    balance(heapq.heapify(heap[:mid-1]))

lesFraFil()