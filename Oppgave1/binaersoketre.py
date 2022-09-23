#Nodeklasse
class Node:

    def __init__(self, dataval) :
        self.dataval = dataval
        self.left = None
        self.right = None

class BinaerSokeTre:

    def __init__(self):
        self.root = None
        self.teller = 0


    def remove(self, v, x):

        if v is None:
            return None
        
        if x < v.dataval:
            v.left = self.remove(v.left, x)
            return v
        
        if x > v.dataval:
            v.right = self.remove(v.right, x)
            return v

        if v.left is None:
            return v.right
        
        if v.right is None:
            if x == self.root.dataval:
                self.root = v.left
            return v.left
        
        
        u = self.FinnMin(v.right)
        v.dataval = u.dataval
        v.right = self.remove(v.right, u.dataval)
        return v



    #Innsetting i et binært søk
    def insert(self, v, x):

        if self.root is None:
            self.root = Node(x)
            self.teller += 1
            return

        if v is None:
            v = Node(x)
            self.teller += 1
        
        elif x < v.dataval:
            v.left = self.insert(v.left, x)
                

        elif x > v.dataval: 
            v.right = self.insert(v.right, x)
                
        return v



    def contains(self, v, x):

        if v is None:
            return None

        if v.dataval == x:
            return v
        
        if x < v.dataval:
            return self.contains(v.left , x)

        if x > v.dataval:
            return self.contains(v.right, x)
        


        # #Basesøk: Noden er null eller elementet er Noden
        # if v is None or v.dataval == x:
        #     return v
        
        # # Verdi i Node er større enn  x

        # if v.dataval < x:
        #     return self.contains(v.right, x)

        # # Verdi i Node er mindre enn x
        # return self.contains(v.left, x)




    def FinnMin(self, v):

        if v is None:
            return v

        curr = v

        while (curr.left is not None):
            curr = curr.left
        
        return curr

    
    def leggTil(self):
        self.teller += 1
    
    def trekkFra(self):
        self.teller -=1
    
    def size(self):
        return self.teller
