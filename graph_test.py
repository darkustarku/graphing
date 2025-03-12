import pytest
import nodes as nd

sample_edges = [ [0,1], [0,6], [0,8], [1,4], [1,6], [1,9], [2,4], [2,6], [3,4], [3,5],
[3,8], [4,5], [4,9], [7,8], [7,9] ]

sample_answer = {0: {1, 6, 8}, 
                 1: {0, 4, 6, 9}, 
                 2: {4, 6},
                 3: {4, 5, 8},
                 4: {1, 2, 3, 5, 9},
                 5: {3, 4},
                 6: {0, 1, 2},
                 7: {8, 9},
                 8: {0, 3, 7},
                 9: {1, 4, 7}}

def test_convert_nodes():
    AdjList = nd.convertNodes(sample_edges)
    for i in range(len(AdjList.keys())):
        assert set(AdjList[i]) == sample_answer[i]

