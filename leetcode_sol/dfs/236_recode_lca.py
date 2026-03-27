'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.ans = None

    def lca(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(curr: TreeNode):
            if not curr:
                return False
            
            left = curr.left
            right = curr.right
            
            node = curr == p or curr = q
            if node + left + right >= 2:
                self.ans = curr
            return node or left or right
        dfs(root)
        return self.ans

