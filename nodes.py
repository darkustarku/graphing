import random as random
import numpy as num 
from display import CANVAS_WIDTH, CANVAS_HEIGHT

class NodeList():

    class Node():

        def __init__(self, coords, value, neighbors):
            self.coords = coords 
            self._value = value
            self._neighbors = neighbors 
        
        def getCoords(self):
            return self.coords
        
        def getValue(self):
            return self.value 
        
        def getNeighbors(self):
            return self._neighbors
        
    def createNodeList(self, AdjList):
        nodelist = []
        for value in AdjList:
            x = random.randint(0, CANVAS_WIDTH)
            y = random.randint(0, CANVAS_HEIGHT)
            neighbors = AdjList[value]
            coords = num.array([x, y])
            new_node = NodeList.Node(coords, value, neighbors)
            nodelist.append(new_node)

        return nodelist

    def __init__(self, AdjList):
        self._data = self.createNodeList(AdjList)
        self._size = len(self._data)
    
    def numNodes(self):
        return self._size
    
    def printNodes(self):
        for node in self._data:
            print(f"Node value is: {node._value}    It is positioned at {node.getCoords()} and has neighbors {node._neighbors}")


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



