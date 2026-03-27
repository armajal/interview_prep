'''

You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. 

This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. 
These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. 
Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.
root = node
for node in list
    
    dfs(root, node)
        if node has child:
            dfs(node, child)
        if node does not have child:
            root.next = node
            node.prev = root


    

'''

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
def flatten_doubly_linked_list(head:Node) -> Node:
    if head is None:
        return head
    
    def dfs(root: Node, curr: Node):
        if curr is None:
            return root
    
        root.next = curr
        curr.prev = root
        tempNxt = curr.next
        
        tail = dfs(curr, curr.child)
        curr.child = None

        return dfs(tail, tempNxt)
    
    
    new_head = Node(-1, None, head, None)
    
    
    dfs(new_head, head)
    new_head.next.prev = None
    return new_head.next
            

