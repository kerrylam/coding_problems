# Given a 2d grid map of '1's (land) and '0's (water), 
# count the number of islands. 
# An island is surrounded by water and is formed by connecting 
# adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: [[1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0],[0,0,0,0,0]]

# Output: 1

# Example 2:

# Input: [[1,1,0,0,0], [1,1,0,0,0], [0,0,1,0,0], [0,0,0,1,1]]

# Output: 3


class MapGridNode():
    def __init__(self, grid, adjacent=None):
        """create a map grid node with another map grid adjacent"""

        if adjacent is None:
            adjacent = []

        assert isinstance(adjacent, list)

        self.grid = grid
        self.adjacent = adjacent

    def __repr__(self):
        """Debugging-friendly representation"""

        return f"<MapGridNode: {self.grid}>"


class MapGraph():
    """Graph showing map grids and their relationships"""

    def __init__(self):

        self.nodes = []

    def __repr__(self):
        return f"<MapGraph: { {m.grid for m in self.nodes} }>"

    def add_grid(self, grid):
        """add grid to the map"""

        self.nodes.append(grid)

    def set_grids(self, grid1, grid2):
        """set the order of grids on the map"""

        grid1.adjacent.append(grid2)


def count_islands(list_of_grid_nodes):
    """Given a list of grid nodes, count how many islands exist on that map"""

    for grid in list_of_grid_nodes:
        map_grid = MapGridNode(grid)
        



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        for x_index, row in enumerate(grid):
            for y_index, square in enumerate(row):
                if square == '1': 
                    island_count += 1
                    self.mark_all_connected_stuff(x_index, y_index, grid)
        return island_count 
    def mark_all_connected_stuff(self, x, y, grid): 
        places_to_go = [(x, y)]
        while places_to_go: # while theres still square to check
            x, y = places_to_go.pop() # grab a square to process 
            # make sure that square is in bounds and a 1
            if (x >= 0 and y >= 0 and 
               x < len(grid) and 
               y < len(grid[0]) and
               grid[x][y] == '1'): 
                # marking this square as seen on our grid
                grid[x][y] = 'x'
                # put all squares connected to it in our list of places we need to check out
                places_to_go.append((x + 1, y)) # DOWN
                places_to_go.append((x - 1, y)) # UP
                places_to_go.append((x, y + 1)) # RIGHT
                places_to_go.append((x, y - 1)) # LEFT



def andrews_dfs_iterative(graph_node):
    stack = [graph_node]
    seen = set()
    while stack:
        current = stack.pop()
        if current not in seen: 
            seen.add(current)
            # DO SOME STUFF, whatever we want
            print(current.val)
            for child in current.children: 
                stack.append(child)
import deque from collections
def andrews_bfs_iterative(graph_node):
    q = deque()
    q.append(graph_node)
    seen = set()
    while q:
        current = q.popleft()
        if current not in seen: 
            seen.add(current)
            # DO SOME STUFF, whatever we want
            print(current.val)
            for child in current.children: 
                q.append(child)
def andrews_dfs_recursive(graph_node, seen = set()):
    if graph_node in seen: return
    seen.add(graph_node)
    print(graph_node.val)
    for child in graph_node.children:
        andrews_dfs_recursive(child, seen)







