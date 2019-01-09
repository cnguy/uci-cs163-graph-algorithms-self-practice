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

# O(1)
def get_neighbors(g, v):
    return g[v]

# overall time complexity: O(|V| + |E|) [THETA TIGHT BOUND]
# visited: O(|V|) space complexity
def dfs_helper(g, v, visited):
    print(v)
    visited.append(v)
    # `get_neighbors` depends on the graph implementation. In this case,
    # we're using an adjacency list, and so getting a list of
    # neighbor vertices is O(1).
    #
    # This is important because that's the pro of adjacency lists. However,
    # they are not good at quickly stating if 2 vertices `x` and `y` are adjacent,
    # as you have to iterate over the list of neighbor vertices to determine this.
    ns = get_neighbors(g, v)
    for n in ns:
        if n not in visited:
            dfs_helper(g, n, visited)

def dfs(g, root):
    dfs_helper(g, root, [])

if __name__ == '__main__':
    dfs(graphs[0], 'A')
    print()
    dfs(graphs[1], 'A')