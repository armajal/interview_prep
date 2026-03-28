'''
* Use when you you have to exhast decision space 
* Get all, recurse 
1. Have a Core Choice
    - reduce the decision space 
2. Constraints
    - define what is valid in every decision space

3. Recurse
    - visit the neext reasonable decision if valid or not. 

- Algo:
 Res = [], Ending resolution wit Valid decisions from either leaves, or base case decisions 
 Curr = [], 
  
  1. Make a choice
    A. Go left (no to choice)

    B. Go Right, (yes to choicee)
 2. Append 

 
Giveen an integer array num of unique eleemnts return posible susbets w/o duplicates 
'''

def subsets(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    res = []
    path = []


    def dfs(idx):
        if idx == n:
            res.append(path[:])
            return
        
        # Dont pick nums[idx]
        dfs(idx + 1)

        # Pick nums
        path.append(nums[idx])
        dfs(idx+1)
        path.pop()

    dfs(0) # Time O(2^n), Space: O(n) Recusrive Depth == Space in call Stack
    return res
arr = [1,2,3]
print(subsets(arr))
        
            

            
