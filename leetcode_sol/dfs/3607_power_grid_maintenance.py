'''
You are given an integer c representing c power stations, each with a unique identifier id from 1 to c (1‑based indexing).

These stations are interconnected via n bidirectional cables, represented by a 2D array connections, 
where each element connections[i] = [ui, vi] indicates a connection between station ui and station vi. 
Stations that are directly or indirectly connected form a power grid.

Initially, all stations are online (operational).

You are also given a 2D array queries, where each query is one of the following two types:

[1, x]: A maintenance check is requested for station x. If station x is online, it resolves the check by itself. 
If station x is offline, the check is resolved by the operational station with the smallest id in the same power grid as x. 
If no operational station exists in that grid, return -1.

[2, x]: Station x goes offline (i.e., it becomes non-operational).

Return an array of integers representing the results of each query of type [1, x] in the order they appear.

Note: The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.
Example 1:

Input: c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]

Output: [3,2,3]

Explanation:
Initially, all stations {1, 2, 3, 4, 5} are online and form a single power grid.
Query [1,3]: Station 3 is online, so the maintenance check is resolved by station 3.
Query [2,1]: Station 1 goes offline. The remaining online stations are {2, 3, 4, 5}.
Query [1,1]: Station 1 is offline, so the check is resolved by the operational station with the smallest id among {2, 3, 4, 5}, which is station 2.
Query [2,2]: Station 2 goes offline. The remaining online stations are {3, 4, 5}.
Query [1,2]: Station 2 is offline, so the check is resolved by the operational station with the smallest id among {3, 4, 5}, which is station 3.
Example 2:

Input: c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]

Output: [1,-1]

Explanation:

There are no connections, so each station is its own isolated grid.
Query [1,1]: Station 1 is online in its isolated grid, so the maintenance check is resolved by station 1.
Query [2,1]: Station 1 goes offline.
Query [1,1]: Station 1 is offline and there are no other stations in its grid, so the result is -1.
 
'''
class Vertex:
    def __init__(self, vertex_id: int = None):
        self.vertex_id = vertex_id
        self.offline = False
        self.power_grid_id = -1
        if vertex_id is not None:
            self.vertex_id = vertex_id


class Graph:
    def __init__(self):
        self.adj: Dict[int, List[int]] = {}
        self.vertices: Dict[int, Vertex] = {}

    def add_vertex(self, id: int, value: Vertex):
        self.vertices[id] = value
        self.adj[id] = []

    def add_edge(self, u: int, v: int):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def get_vertex_value(self, id: int) -> Vertex:
        return self.vertices[id]

    def get_connected_vertices(self, id: int) -> List[int]:
        return self.adj[id]


class Solution:
    def traverse(
        self, u: Vertex, power_grid_id: int, power_grid: List[int], graph: Graph
    ):
        u.power_grid_id = power_grid_id
        heapq.heappush(power_grid, u.vertex_id)
        for vid in graph.get_connected_vertices(u.vertex_id):
            v = graph.get_vertex_value(vid)
            if v.power_grid_id == -1:
                self.traverse(v, power_grid_id, power_grid, graph)

    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        graph = Graph()
        for i in range(c):
            v = Vertex(i + 1)
            graph.add_vertex(i + 1, v)

        for conn in connections:
            graph.add_edge(conn[0], conn[1])

        power_grids = []
        power_grid_id = 0

        for i in range(1, c + 1):
            v = graph.get_vertex_value(i)
            if v.power_grid_id == -1:
                power_grid = []
                self.traverse(v, power_grid_id, power_grid, graph)
                power_grids.append(power_grid)
                power_grid_id += 1

        ans = []
        for q in queries:
            op, x = q[0], q[1]
            if op == 1:
                vertex = graph.get_vertex_value(x)
                if not vertex.offline:
                    ans.append(x)
                else:
                    power_grid = power_grids[vertex.power_grid_id]
                    while (
                        power_grid
                        and graph.get_vertex_value(power_grid[0]).offline
                    ):
                        heapq.heappop(power_grid)
                    ans.append(power_grid[0] if power_grid else -1)
            elif op == 2:
                graph.get_vertex_value(x).offline = True

        return ans

# def power_grid_mainteenance(self, c: int, connections: list[list[int]], queries: list[int]):
#     operational = set(range(len(1, c + 1)))
#     adj = {}

#     def dfs(self, curr: int):
            
#         visited = set()
#         min_online = [-1]
#         def find_min(self, curr):
#             visited.add(curr)

#             if curr in operational:
#                 if min_online[0] == -1 or curr < min_online[0]:
#                         min_online[0] = curr
#             for station in a_map.get(curr, []):
#                 if station not in visited:
#                     self.dfs(station)

#         self.find_min(station)
#         return min_online[0]

#     for connection in connections:
#         a = connection[0]
#         b = connection[1]

#         adj.setdefault(a, []).append(b)
#         adj.setdefault(b, []).append(a)
    
#     ans = []
#     for query in queries:
#         op = query[0]
#         station = query[1]

#         found = []
#         if op == 1:
#             if station in operational:
#                ans.append(station)
            
#             else:
#                 ans.append(self.dfs(station))

#         else:
#             operational.discard(station)

#     return ans
    
    