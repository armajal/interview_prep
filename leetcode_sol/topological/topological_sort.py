'''
Topological Sort: Orders edges in a directed acyclic graph (DAG) such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering. This is useful for scheduling tasks, resolving dependencies, and organizing data hierarchically.
1. Graph must have no cycles
2. Could only have one valid order

Indegrees: Incoming Edges pointing to a vertex 
    Ex: A -> B -> C
    Indegrees: A: 0, B: 1, C: 1

        A -> B,C -> D
        A: 0, B: 1, C: 1, D: 2

Kahn's Algorithm (BFS Variant):
 1. Calculate indegree for all nodes
 2. add all nodes with indegree 0 to queue
 3. while queue not empty, dequeue add to order, decrement neighbor indegrees
 4. Return the topological order 

'''
from collections import deque
from collections import defaultdict

def topological_sort(node_map):
    indegree = defaultdict(int)
    queue = deque()
    order = []

    for node in node_map.keys():
        if node in node_map:
            neighbors = node_map[node]
            for neighbor in neighbors:
                indegree[neighbor] += 1

    for node in range(len(indegree)):
        if indegree[node] == 0:
            queue.append(node)
    
    while queue:
        
        curr = queue.popleft()
        if curr not in node_map:
            continue
        order.append(curr)
        for neighbor in node_map[curr]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return order 

sort_dict = {1: [2, 3], 2: [4], 3:[4], 4:[]}
print(topological_sort(sort_dict))
    



    
