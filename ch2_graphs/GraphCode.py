""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

class Vertex(object):
    """A Vertex is a node in a graph."""

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Edge(tuple):
    """An Edge is a list of two vertices."""

    def __new__(cls, e1, e2):
        """The Edge constructor takes two vertices."""
        return tuple.__new__(cls, (e1, e2))

    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Graph(dict):
    """A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.
    
    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""

    def __init__(self, vs=[], es=[]):
        """Creates a new graph.  
        vs: list of vertices;
        es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)
            
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self[v] = {}

    def add_edge(self, e):
        """Adds and edge to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, v, w):
        """Takes 2 vertices v and w and returns edge e if it exists"""
        try:
            e = self[v][w]
            return e
        except:
            return None

    def remove_edge(self, e):
        """Takes an edge and removes all refrences to it from the graph"""
        for v, self_v in dict(self).items():
            for w, vw_e in dict(self_v).items():
                if(vw_e == e):
                    del self[v][w]
                
    def vertices(self):
        return list(self.keys())

    def edges(self):
        list_of_edges = []
        for v, self_v in dict(self).items():
            for w, vw_e in dict(self_v).items():
                list_of_edges.append(vw_e)
        return list_of_edges

    def out_edges(self, v):
        return list(self[v].values())

    def add_all_edges(self):
        verts = self.vertices()
        tuples = [(v,w) for v in verts for w in verts if v != w]
        for pair in tuples:
            self.add_edge(Edge(pair[0],pair[1]))



def main(script, *args):
    v = Vertex('v')
    w = Vertex('w')
    e = Edge(v, w)
    x = Vertex('x')
    y = Vertex('y')
    z = Edge(x,y)
    g = Graph([v,w,x,y], [e,z])
    print(g.get_edge(x,v))
    print(g.get_edge(x,y))
    print(g)
    print("removing edge \n")
    g.remove_edge(z)
    g.remove_edge(e)
    print(g)
    print("adding all edges back")
    g.add_all_edges()
    print(g)


if __name__ == '__main__':
    import sys
    main(*sys.argv)
