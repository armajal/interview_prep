'''
There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.
'''


def restore_adjacnt_pairs(adjacentPairs: list[list[int]]) -> [int]:
    adj = {}

    for pair in adjacentPairs:
        a = pair[0]
        b = pair[1]
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)

    root = None
    for k in adj.keys():
        if len(adj[k]) == 1:
            root = k
            break

    ans = []
    def dfs(curr: int, prev: int, res: [int]):
        res.append(curr)
        for nxt in adj[curr]:
            if prev != nxt:
                dfs(nxt, curr, res)
    dfs(root, 0, ans)
    return ans

# Test 
adjacentPairs = [[2,1],[3,4],[3,2]]
# Expectd Output: [1,2,3,4]
print(restore_adjacnt_pairs(adjacentPairs))
