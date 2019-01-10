graphs = [
    {
        'A': ['B', 'D'],
        'B': ['C'],
        'C': ['D'],
        'D': [],
    },
    {
        'A': ['B', 'C', 'E'],
        'B': ['D', 'F'],
        'C': ['G'],
        'D': [],
        'E': ['F'],
        'F': ['B', 'E'],
        'G': [],
    },
]

def get_neighbors(g, v):
    return g[v]

# Goes from right to left in a neighbor list (opposite of recursive).
# same time complexity as recursive counterpart
# worst-case space complexity: O(E)
# e.g. graph {"A":["B,C,D,E,F,G"]}
def dfs(g, root):
    s = [root]
    visited = []

    while s:
        v = s.pop()
        if v not in visited:
            print(v)
            visited.append(v)
            ns = get_neighbors(g, v)
            for n in ns:
       #         if n not in visited:
        #            s.append(n)
                s.append(n)

if __name__ == '__main__':
    dfs(graphs[0], 'A')
    print()
    dfs(graphs[1], 'A')