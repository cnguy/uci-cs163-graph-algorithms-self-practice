# An adjacency list that stores neighbors, vertex values, and edge values.
class AdjacencyList:
    def __init__(self):
        self.g = {}
    
    def _make_vertex(self, v, vertexValue, edgeValue):
        return (v, vertexValue, edgeValue)
    def _vertex(self, v):
        return v[0]
    def _vertex_value(self, v):
        return v[1]
    def _edge_value(self, v):
        return v[2]
    
    def adjacent(self, x, y): pass

    # Time complexity: O(|E|)
    def neighbors(self, x):
        if x not in self.g:
            return None # or empty list
        return [self._vertex(v) for v in self.g[x]]

    # Time complexity: O(1)
    def add_vertex(self, x):
        if x in self.g:
            return None 
        self.g[x] = []

    def remove_vertex(self, x): pass

    def add_edge(self, x, y):
        if x not in self.g:
            self.g[x] = []
        if y not in self.g:
            self.g[y] = []
        self.g[x].append(self._make_vertex(y, 0, 0))
        self.g[y].append(self._make_vertex(x, 0, 0))

    def remove_edge(self, x, y): pass
    def get_vertex_value(self, x): pass
    def set_vertex_value(self, x, v): pass

    def get_edge_value(x, y): pass
    def set_edge_value(x, y, v): pass

if __name__ == '__main__':
    a1 = AdjacencyList()
    a1.add_vertex('A')
    print(a1.g['A'])
    a1.add_edge('A', 'B')
    print(a1.g['A'])
    print(a1.g['B'])
    print(a1.neighbors('A'))