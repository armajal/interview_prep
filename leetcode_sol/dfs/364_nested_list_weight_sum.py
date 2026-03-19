'''
You are given a nested list of integers nestedList. Each element is either an integer or a list 
whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list 
[1,[2,2],[[3],2],1] has each integer's value set to its depth. Let maxDepth be the maximum depth of any integer.

The weight of an integer is maxDepth - (the depth of the integer) + 1.

Return the sum of each integer in nestedList multiplied by its weight.

--------------------------------------------------------------------------------------
dfs = down with state, return result


Input: nestedList = [[1,1],2,[1,1]]
Output: 8
Explanation: Four 1's with a weight of 1, one 2 with a weight of 2.
1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8

Input: NestedList of integers
Output: math 
Tool: DFS
Approach
    state = NesstedInteger value + Level -> dfs(NesetedInteger, level)
    sum = 0
    for idx in NestedIntegerList:
       sum += dfs(nestedInteger, level)

    dfs(nestedInteger, level):
        if level == NestedInteger:
         return level * NestedInteger.isInteger
        
        return dfs(nestInteger, level +1)
'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        
        def get_depth(nested, level):
            if nested.isInteger():
                return level
            return max(get_depth(el, level + 1) for el in nested.getList())

        max_depth = max(get_depth(n, 1) for n in nestedList)

        def dfs(nestedValue, level):
            total = 0
            if nestedValue.isInteger():
                return (max_depth - level + 1) * nestedValue.getInteger()
            for nested in nestedValue.getList():
                total += dfs(nested, level + 1)
        
            return total
        
        return sum(dfs(nested, 1) for nested in nestedList)