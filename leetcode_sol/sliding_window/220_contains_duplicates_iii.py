'''
You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:

i != j,
abs(i - j) <= indexDiff.
abs(nums[i] - nums[j]) <= valueDiff, and
Return true if such pair exists or false otherwise.

 
# 15:43 start
Input: nums[], indexDDiff, valueDiff
Output: True/False
Constraint: i !=j, abs(i-j) <= indexDiff, abs(nums[i] - nums[j]) <= valueDiff
Tool:


[0 1 5 6 10 29] indexDiff = 8, valueDiff = 20
Brute Force:
    i = 0, j = 0 
    for i in arr:
        for j in arr:
            if( i != j and valuesDiffCheck(i,j, nums) and indexDiff(i, j, nums))
                return true
    return false

Bucket Solution
 bucket = {}
 start = 0 
 size = valuesDiff + 1
 for i, num in enumerate(nums):
    b = get_bucket(num)
    
    if b in buckets:
        return true

    if b - 1 in buckets and abs(num - buckets[b -1]) <= valuesDiff:
        return True
    
    if b + 1 in buckets and abs(num - buckets[b + 1]) <= valuesDiff:
        return True
    
    bucket[b] = num

    if i >= indexDiff:
        del buckets[get_bucket(nums[i - indexDiff])]

        return false

get_bucket:
    num => 0
        return num // size
    return (num + 1) // (size - 1)


'''
from sortedcontainers import SortedSet
from bisect import bisect_left
import defaultdict
class Solution:
    def __init__(self):
        return
    
    def contains_duplicates_iii(self, nums: [int], valuesDiff:int, indexDiff: int) -> bool: 
        i = 0
        j = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and self.valuesDiffCheck(i,j, nums, valuesDiff) and self.indexDiffCheck(i, j, indexDiff):
                    return True
        return False
    
    def valuesDiffCheck(self, x: int, y:int, arr:[], valuesDiff: int):
        return abs(arr[x] - arr[y]) <= valuesDiff

    def indexDiffCheck(self, x: int, y:int, indexDiff: int):
        return abs(x - y) <= indexDiff

    
    def contains_duplicates_iii_w_sliding_window(self, nums: [int], valuesDiff:int, indexDiff: int) -> bool:
        window = SortedSet()
        left = 0

        for num in nums:
            pos = window.bisect_left(num - valuesDiff)
            if pos < len(window) and window[pos] <= num + valuesDiff:
                return True
            
            window.add(num)
            if len(window) > indexDiff:
                window.remove(nums[left])
                left += 1
        return False
    
    def contains_duplicates_iii_bucket(self, nums:[int], valuesDiff: int, indexDiff: int) -> bool:
        if valuesDiff < 0:
            return False
        
        #We use buckets to organize our values into "close enough" values
        buckets = {}        # stores bucket_id -> num in the sliding window
        size = valuesDiff + 1 # +1 is so we are in within the window and anything onthe border is caught because it is <=
        left = 0 
        for right, num in enumerate(nums): # go through nums, num for quick reference and right because index is our pointer
            def get_bucket(num):
                return num // size        # python handles negative integer division
        
            bucket = get_bucket(num)

            if bucket in buckets: #we are in the same bucket, which means the value and index are close enough
                return True

            for adj_bucket in [bucket - 1, bucket + 1]: # the next bucket that's small and the next largest bucket because then we know it is +/-

                if adj_bucket in buckets and abs(num - buckets[adj_bucket]) <= valuesDiff: #if bucket even exists and whatever value in that bucket is within valuesDiff, we are good
                    return True
                
            buckets[bucket] = num #Add num to the values bucket if we didn't find anything. could be another pair
            
            if right - left >= indexDiff: #We slide our window like normal to constrain the options
                left_num = nums[left]
                old_bucket = get_bucket(left_num)
                del buckets[old_bucket]
                left += 1

        return False
    
  

solution = Solution()


# Test 1 |  True |
#Brute Force Passes 15:59
# nums = [1,2,3,1]
# indexDiff = 3
# valueDiff = 0
# print(solution.contains_duplicates_iii(nums, valueDiff, indexDiff))

# # Test 2 | False | 
# # Brute Force Failed 15:59 | Fixed copy and paste bug
# nums2 = [1,5,9,1,5,9]
# indexDiff2 = 2
# valueDiff2 = 3
# print(solution.contains_duplicates_iii(nums2, valueDiff2, indexDiff2))
#All Test Passed w/ @ 16:03 brute force


#--------------------- Sliding Window Tests @ 16:10--------------
nums = [1,2,3,1]
indexDiff = 3
valueDiff = 0
print(solution.contains_duplicates_iii_w_sliding_window(nums, valueDiff, indexDiff))





'''
Tests:
Example 1:

Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
Example 2:

Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.


Truthfully this took hours, a couple of youtube videos to understand and claude. I took a break and came back anc it took a while to get it. 


'''