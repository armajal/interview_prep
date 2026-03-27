'''
Given the root of a binary search tree, return a balanced binary search tree with the same node values. 
If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.



'''
class TreeNode:
    def __init__(self, val: int, left= None, right = None):
        self.val = val
        self.left = left
        self.right = right
def balance_binary_st(root: TreeNode) -> TreeNode:
    inorder = []

    def inorder_dfs(curr: TreeNode):
        if not curr:
            return
        
        
        inorder_dfs(curr.left)
        inorder.append(curr.val)
        inorder_dfs(curr.right)

    inorder_dfs(root)

    left, right = 0, len(inorder) - 1
    
    def get_node(l, r):
        if l > r:
            return None
        mid_idx = l + r // 2
        curr_node = TreeNode(inorder[mid_idx])
        

        curr_node.left = get_node(l, mid_idx -1)
        curr_node.right = get_node(mid_idx + 1, r)
        return curr_node
    return get_node(left, right)
four = TreeNode(4)
three = TreeNode(3, four)
two = TreeNode(2, three)
one = TreeNode(1, two)

balance_binary_st(one)

