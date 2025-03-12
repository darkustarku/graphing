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
    


sampleEdges = [ [0,1], [0,6], [0,8], [1,4], [1,6], [1,9], [2,4], [2,6], [3,4], [3,5],
[3,8], [4,5], [4,9], [7,8], [7,9] ]

def convertNodes(edgeList):
    graph = {}

    for edge in edgeList:
        (first, second) = edge
        if (first not in graph):
            graph[first] = set()
        if (second not in graph):
            graph[second] = set()
        graph[first].add(second)
        graph[second].add(first)
    
    return graph  



