import Graph
import random
class RandomGraph(Graph.Graph):
    def __init__(self, vs=[]):
        super().__init__(vs)

    def add_random_edge(self, p):
        """Add edge to graph with probability p"""
        #Loop through every combination of vertice
        verts = self.vertices()
        tuples = [(v,w) for v in verts for w in verts if v!= w]
        for pair in tuples:
            print(pair)
            if(random.uniform(0,1) <= p):
                self.add_edge(Graph.Edge(pair[0], pair[1]))
