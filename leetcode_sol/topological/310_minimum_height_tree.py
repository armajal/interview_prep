'''
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, 
any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that 
there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. 

When you select a node x as the root, the result tree has height h.
Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

#12:51pm 
Input : n nodes, edges[] edge[i] -> [a,b]
Output : [] of all MHT Roots, in any order 
Constraint: MHT -> min(h) root-> leaf.
            Toplogical Sort is only needed here for the component of indegrees. Indegrees help us to understand the degrees of incoming nodes and their relationship

            We use the indgree to determine the leaves. So we can use it to build up the tree from leaf to root. Appending nodes as thhey become the leeaf until w ehave 2 nodes left. 
Approach:
    0. adj_list = {}, min_height = 0, indegree = n * [0]
    if you know the indegree you can know how often things come into the node
        indegreee order 
    
    1. Build an adj_list of nodes each direction and indegrees[n]
    2. enqueue any nodes w/ indegree == 1 bc those are leaves
    3. queue for n with the indegrees == 1:
            queue = [n] n being the node with the most indegrees
            min_height = toplogical sort from n


    
Time Complexity
Space Complexity
Test Cases:
    Input: n = 4, edges = [[1,0],[1,2],[1,3]]
      
Edge Cases

'''
from collections import deque
def minimum_height_tree(n: int, edges:[[int]]) -> [int]:
    if n is None or n == 0 or edges is None:
        return -1
    
    adj_list = {}
    mhts = []
    degree = [0] * n
    for edge in edges:
        a = edge[0]
        b = edge[1]
        adj_list.setdefault(a, []).append(b)
        adj_list.setdefault(b, []).append(a)
    
    
    for k, v in adj_list.items():
        degree[k] += 1

    leaf_queue = deque([i for i in range(n) if len(adj_list[i]) == 1])

    remaining = n
    while remaining > 2:
        remaining -= len(leaf_queue)
        new_leaves = deque()

        while leaf_queue:
            leaf = leaf_queue.popleft()
            neighbor = adj_list[leaf][0]
            adj_list[neighbor].remove(leaf)
            if len(adj_list[neighbor]) == 1:
                    new_leaves.append(neighbor)
        
        leaf_queue = new_leaves

    return list(leaf_queue)
'''
[[1,0],[1,2],[1,3]]                                             adj_list = {0: 1, 1: 0,2,3, 2: 1, 3:1}

       0                3                   1
       1                1               2   3   0
    2     3         2       0

indegree  [ 1   3   1   1 ]
            0   1   2   3    

queue =   0, 2, 3
        1
curr_min = 1
visited = 1
min_len = 

'''

n = 4
edges = [[1,0],[1,2],[1,3]]
# Expected Output: [1]
print(minimum_height_tree(n, edges))