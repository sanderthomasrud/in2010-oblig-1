import sys
from Teque import *



teque = Teque()
 
for line in sys.stdin:
    words = line.split()
    if "push_back" in line:
        teque.push_back(words[1])
    elif "push_middle" in line:
        teque.push_middle(words[1])
    elif "push_front" in line:
        teque.push_front(words[1])
    elif "get" in line:
        print(teque.get(int(words[1])))