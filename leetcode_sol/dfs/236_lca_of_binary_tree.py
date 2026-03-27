'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T
 that has both p and q as descendants (where we allow a node to be a descendant of itself).”

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def find_lca(p: TreeNode, q: TreeNode, root: TreeNode):
    '''
    dfs tree
    keep visited until found
    return min of union sset 
    
    '''
    def dfs(self, node: TreeNode, target: TreeNode, visited: set()):
        if node == target:
            return
        visited.add(node)
        dfs(node.left, target, visited)
        dfs(node.right, target, visited)
        return
    visited_p = set()
    visited_q = set()
    ans = list(dfs(root, p, visited_p) & dfs(root, q, visited_q))
    return ans[0]