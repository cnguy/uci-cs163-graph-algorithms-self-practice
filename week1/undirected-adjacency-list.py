# An adjacency list that stores neighbors, vertex values, and edge values.
class AdjacencyList:
    def __init__(self):
        self.g = {}
    
    # A vertex in this case will be represented as a mutable tuple [vertex_value, neighbors].
    # Each neighbor is represented as a tuple [vertex_name, edge_value].
    # e.g
    # { A: (5, [('B', 4)] }
    # A has a vertex value of 5.
    # Edge AB has a value of 4.
    def _make_vertex(self, v_value, neighbors):
        return [v_value, neighbors]
    def _make_neighbor(self, n, e_value):
        return [n, e_value]
    def _vertex_value(self, v):
        return v[0]
    def _neighbor_id(self, n):
        return n[0]
    def _edge_value(self, n):
        return n[1]
    def _set_edge_value(self, n, v):
        n[1] = v
    
    # O(|E|)
    def adjacent(self, x, y):
        # This graph is undirected, so we don't have to loop over self.g[y].
        for n in self.g[x][1]:
            if self._neighbor_id(n) == y:
                return True
        return False

    # O(|E|)
    def neighbors(self, x):
        if x not in self.g:
            return None # or empty list
        return [self._neighbor_id(n) for n in self.g[x][1]]

    # O(1)
    def add_vertex(self, x):
        if x in self.g:
            return None 
        self.g[x] = self._make_vertex(0, [])

    # O(|E|)
    def remove_vertex(self, x):
        # O(|E|) for directed graphs using a linked list,
        # but in this undirected case, it seems like O(|V| * |E| * O(pop)).
        for i in range(0, len(self.g[x][1])):
            n = self._neighbor_id(self.g[x][1][i])
            for j in range(0, len(self.g[n][1])):
                if self._neighbor_id(self.g[n][1][j]) == x:
                    self.g[n][1].pop(j)

        self.g.pop(x, None) # Let's say this is O(1)

    # O(1) append (with a linked list or high-capacity array for example)
    def add_edge(self, x, y):
        if x not in self.g:
            self.g[x] = self._make_vertex(0, [])
        if y not in self.g:
            self.g[y] = self._make_vertex(0, [])
        self.g[x][1].append(self._make_neighbor(y, 0))
        self.g[y][1].append(self._make_neighbor(x, 0))

    # O(|V|) in directed, linked list-based graph, but in this case
    # O(|V| * O(pop) + O|V| * O(pop)) is O(|V| * O(pop))
    def remove_edge(self, x, y):
        for i in range(0, len(self.g[x][1])):
            if self._neighbor_id(self.g[x][1][i]) == y:
                self.g[x][1].pop(i)
        for i in range(0, len(self.g[y][1])):
            if self._neighbor_id(self.g[y][1][i]) == x:
                self.g[y][1].pop(i)

    # O(1)
    def get_vertex_value(self, x):
        return self._vertex_value(self.g[x])

    # O(1)
    def set_vertex_value(self, x, v):
        self.g[x][0] = v

    # O(|E|)
    def get_edge_value(self, x, y):
        for n in self.g[x][1]:
            if self._neighbor_id(n) == y:
                return self._edge_value(n)

    # O(|E|)
    def set_edge_value(self, x, y, v):
        for n in self.g[x][1]:
            if self._neighbor_id(n) == y:
                self._set_edge_value(n, v)

if __name__ == '__main__':
    a1 = AdjacencyList()
    a1.add_vertex('A')
    print(a1.g['A'])
    a1.add_edge('A', 'B')
    print(a1.g['A'])
    print(a1.g['B'])
    print(a1.neighbors('A'))
    print(a1.adjacent('A', 'B'))
    print(a1.get_vertex_value('A'))
    print(a1.get_edge_value('A', 'B'))
    a1.set_edge_value('A', 'B', 20)
    print(a1.get_edge_value('A', 'B'))
    print(a1.get_vertex_value('A'))
    a1.set_vertex_value('A', 5)
    print(a1.get_vertex_value('A'))
    print(a1.neighbors('A'))
    print(a1.neighbors('B'))
    a1.remove_vertex('A')
    print('rm vertex')
    print(a1.neighbors('A'))
    print(a1.neighbors('B'))
    a1.add_vertex('A')
    a1.add_edge('A', 'B')
    print(a1.neighbors('A'))
    print(a1.neighbors('B'))
    a1.remove_edge('A', 'B')
    print(a1.neighbors('A'))
    print(a1.neighbors('B'))
    print(a1.get_vertex_value('A'))