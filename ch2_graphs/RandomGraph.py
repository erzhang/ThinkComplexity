import string
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
            if(random.uniform(0,1) <= p):
                self.add_edge(Graph.Edge(pair[0], pair[1]))

def main(script, n='6', *args):
    p_list = [p/100 for p in range(100)]
    total_exp = 0
    total_connected = 0
    for n in range(1,20):
        for p in p_list:
            total_exp += 1
            # create n Vertices
            n = int(n)
            labels = string.ascii_lowercase + string.ascii_uppercase
            vs = [Graph.Vertex(c) for c in labels[:n]]
            # create a graph 
            g = RandomGraph(vs)
            g.add_random_edge(p)

            if(g.is_connected()):
                total_connected += 1

    print(total_connected/total_exp)

if __name__ == '__main__':
    import sys
    main(*sys.argv)

