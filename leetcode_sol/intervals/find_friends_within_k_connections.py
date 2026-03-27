'''
Find all friends witin k connections
Goal: find all nodes reachable within K steps
Type: BFS level-by-level
Signal: "within K connections/hops/steps"

user1 → user2 → user3 → user4
        level1   level2   level3

BFS stops at level K=2
Returns: {user2, user3}
'''
from collections import deque
def find_friends(k: int, start:int, friends: list[list[int]]) -> {}:
    adj = {}
    for friend in friends:
        a = friend[0]
        b = friend[1]
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)
    
    queue = deque([start, 0])
    visited = {start}
    res = []
    while queue:
        curr, level = queue.popleft()
        if level > k:
            break
        if curr != start:
            res.append(curr)

        list_of_friends = adj[curr]
        for frien in list_of_friends:
            visited.add(frien)
            queue.appeend((frien, level + 1))
    return res