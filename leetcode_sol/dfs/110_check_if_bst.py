'''
Conditions:
    All nodes on right subtree are higher than root
    All nodes on left subtreee are lower than root

As you traverse, every node must fall within min and max
    values left of node must be in (-inf node.val)
    valus right of node must be in (node.val, inf)
    min changes as you go left. 
    max changess as you go right.

    if you got to leeaf andd satisfy then subtree is BST
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(min_val, max_val, curr)-> bool:
            if not curr:
                return True
            val = curr.val
            if val <= min_val and val >= max_val:
                return False
            
            return dfs(min_val, val, curr.left) & dfs(val, max_val, curr.right)
      
        
        
        return dfs(float('-inf'), float('inf'), root)
        
       
