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
    def _id(self, n):
        return n[0]
    def _edge_value(self, n):
        return n[1]
    def _set_edge_value(self, n, v):
        n[1] = v
    
    # O(|E|)
    def adjacent(self, x, y):
        for n in self.g[x][1]:
            if self._id(n) == y:
                return True
        for n in self.g[y][1]:
            if self._id(n) == y:
                return True
        return False

    # O(|E|)
    def neighbors(self, x):
        if x not in self.g:
            return None # or empty list
        return [self._id(n) for n in self.g[x][1]]

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
            n = self._id(self.g[x][1][i])
            for j in range(0, len(self.g[n][1])):
                if self._id(self.g[n][1][j]) == x:
                    self.g[n][1].pop(j)

        self.g.pop(x, None) # Let's say this is O(1)

    # O(1) append (with a linked list or high-capacity array for example)
    def add_edge(self, x, y):
        if x not in self.g:
            self.g[x] = self._make_vertex(0, [])
        self.g[x][1].append(self._make_neighbor(y, 0))

    # O(|V|) in directed, linked list-based graph
    def remove_edge(self, x, y):
        for i in range(0, len(self.g[x][1])):
            if self._id(self.g[x][1][i]) == y:
                self.g[x][1].pop(i)

    # O(1)
    def get_vertex_value(self, x):
        return self._vertex_value(self.g[x])

    # O(1)
    def set_vertex_value(self, x, v):
        self.g[x][0] = v

    # O(|E|)
    def get_edge_value(self, x, y):
        for n in self.g[x][1]:
            if self._id(n) == y:
                return self._edge_value(n)

    # O(|E|)
    def set_edge_value(self, x, y, v):
        for n in self.g[x][1]:
            if self._id(n) == y:
                self._set_edge_value(n, v)

    # Helper functions like these are to abstract the logic
    # so that the code looks like pseudocode that can be written on a test,
    # and be used for running actual code.
    def _pop(self, s):
        return self._id(s.pop())
    def _add_visited(self, v, visited):
        visited.append(self._id(v))

    def dfs_reachable_nodes(self, x):
        x = self._id(x)
        s = [x]
        visited = []
        while s:
            v = self._pop(s)
            if v not in visited:
                visited.append(v)
                ws = self.neighbors(v)
                for w in ws:
                    s.append(self._id(w))
        return visited
    
    def dfs_reachable_nodes_recursive(self, root):
        self.visited = []

        def recurse(v):
            v = self._id(v)
            self.visited.append(v)
            ws = self.neighbors(v)
            for w in ws:
                if w not in self.visited:
                    recurse(w)

        recurse(root)
        return self.visited

if __name__ == '__main__':
    # a1 = AdjacencyList()
    # a1.add_vertex('A')
    # a1.add_vertex('B')
    # a1.add_edge('A', 'B')
    # print(a1.neighbors('A'))
    # print(a1.neighbors('B'))
    # print(a1.neighbors('C'))
    # print(a1.reachable_nodes('A'))
    # a1.add_vertex('C')
    # a1.add_edge('B', 'C')
    # print(a1.reachable_nodes('A'))
    # print(a1.reachable_nodes('B'))
    a2 = AdjacencyList()
    a2.add_vertex('S')
    a2.add_vertex('A')
    a2.add_vertex('D')
    a2.add_vertex('B')
    a2.add_vertex('E')
    a2.add_vertex('F')
    a2.add_edge('S', 'A')
    a2.add_edge('A', 'D')
    a2.add_edge('A', 'B')
    a2.add_edge('B', 'E')
    a2.add_edge('B', 'F')
    print(a2.dfs_reachable_nodes('S'))
    print(a2.dfs_reachable_nodes('A'))
    print(a2.dfs_reachable_nodes('B'))
    print(a2.dfs_reachable_nodes('F'))

    # cs 163 example
    a3 = AdjacencyList()
    a3.add_vertex('S')
    a3.add_vertex('A')
    a3.add_vertex('C')
    a3.add_vertex('D')
    a3.add_vertex('B')
    a3.add_vertex('E')
    a3.add_vertex('F')
    a3.add_edge('S', 'A')
    a3.add_edge('S', 'B')
    a3.add_edge('A', 'B')
    a3.add_edge('B', 'A')
    a3.add_edge('C', 'S')
    a3.add_edge('A', 'D')
    a3.add_edge('B', 'E')
    a3.add_edge('D', 'F')
    a3.add_edge('E', 'F')
    print(a3.dfs_reachable_nodes_recursive('S'))
    print(a3.dfs_reachable_nodes('S'))
    print(a3.neighbors('S'))
    print(a3.neighbors('A'))
    print(a3.neighbors('B'))
    print(a3.dfs_reachable_nodes_recursive('C'))
