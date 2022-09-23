class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data



class Teque:
    def __init__(self):
        self.first = None
        self.middle = None
        self.last = None
        self.size = 0
        self.left = 0
        self.right = 0
    
    def push_front(self, x):
        nodeAdded = Node(x)

        if self.size == 0:
            self.size0(nodeAdded)
            
        elif self.size == 1: 
            self.first = nodeAdded
            self.first.next = self.last
            self.last.prev = self.first
            self.middle = self.last
        else:
            self.first.prev = nodeAdded
            nodeAdded.next = self.first
            self.first = nodeAdded
            
            #changing middlepointer depending on its value 
            self.left +=1
            if self.left - self.right > 1:
                self.middle = self.middle.prev

                self.left -=1
                self.right +=1
        self.size += 1


    def push_middle(self, x):
        nodeAdded = Node(x)

        if self.size == 0:
            self.size0(nodeAdded)
            
        elif self.size == 1: 
            self.last = nodeAdded
            self.first.next = self.last
            self.last.prev = self.first
            self.middle = self.last

        elif self.size == 2:
            self.first.next = nodeAdded
            self.last.prev = nodeAdded
            nodeAdded.next = self.last
            nodeAdded.prev = self.first
            self.middle = nodeAdded
        
        else: 
            if self.left == self.right:
                nodeAdded.next = self.middle.next
                self.middle.next.prev = nodeAdded
                self.middle.next = nodeAdded
                nodeAdded.prev = self.middle
                self.middle = nodeAdded
                self.left += 1
            else:
                self.middle.prev.next = nodeAdded
                nodeAdded.prev = self.middle.prev

                self.middle.prev = nodeAdded
                nodeAdded.next = self.middle
                self.middle = nodeAdded
                self.right += 1
        self.size +=1
                
    def push_back(self, x):
        nodeAdded = Node(x)
        
        if self.size == 0:
            self.size0(nodeAdded)
            
        elif self.size == 1: 
            self.last = nodeAdded
            self.first.next = self.last
            self.last.prev = self.first
            self.middle = self.last
        else:
            self.last.next = nodeAdded
            nodeAdded.prev = self.last
            self.last = nodeAdded
            
            self.right +=1
            if self.right > self.left:
                self.middle = self.middle.next
                self.left +=1
                self.right -=1
        self.size += 1
        
    def get(self, index):
        cur = self.first
        if index>self.size:
            return None
            
        for _ in range(index):
            cur = cur.next
        return cur.data

            
    def size0(self, nodeAdded):
        self.first = nodeAdded
        self.middle = self.first
        self.last = self.first
