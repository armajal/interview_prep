'''
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.
'''

'''

sums = []
setup(root):
    total = dfs(root)
    for s in all_sums:
        val = max(best, s * total - s)
    return val % (10 ** 9 + 7)

dfs(node):
    
    if root is None:
        return 0

    
    left += dfs(node.left)
    right += dfs(node.right)
    total_sum = node.val + left + right
    sums.append[total_sum]
    return total_sum

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
   
def max_splittd_bt(self, root: TreeNode) -> int:
    sums = []
    best = 0

    def dfs(curr: TreeNode):
        if root is None:
            return 0
        left = dfs(curr.left)
        right = dfs(curr.right)
        curr_sum = curr.val + right + left
        sums.append(curr_sum)
        return curr_sum
    
    total_sum = dfs(root)

    for s in sums:
        best = max(best, s * (total_sum - s))
    return best % (10 ** 9 + 7)
   

