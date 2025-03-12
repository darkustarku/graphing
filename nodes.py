class NodeList():

    class Node():

        def __init__(self, x, y, value):
            self._x = x
            self._y = y
            self._value = value
            self._neighbors = [] 
        
        def getCoords(self):
            return (self.x, self.y)
        
        def getValue(self):
            return self.value 
        
        def getNeighbors(self):
            return self._neighbors
        

    def __init__(self):
        self._data = []
        self._size = 0
    
    def numNodes(self):
        return self._size
    
    

