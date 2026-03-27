'''

Given an array of intervals where intervals[i] = [starti, endi],
 merge all overlapping intervals, and return an array of the 
 non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: 

'''

def mergeIntervals(intervals: list[list[int]]) -> list[list[int]]:
    new_intvs = sorted(intervals, key= lambda intv: intv[0])
    stack = []
    
    for intv in new_intvs:
        end = intv[1]
        start = intv[0]

        if stack and stack[-1][1] >= start:
            curr = stack.pop()
            new_intv = [curr[0], max(curr[1], end)]
            stack.append(new_intv)
        
        else:
            stack.append(intv)
    return stack

test1_intervals = [[1,3],[2,6],[8,10],[15,18]]
print(mergeIntervals(test1_intervals))

test2_intervals = [[1,4],[4,5]]
print(mergeIntervals(test2_intervals))

test3_intervals = [[4,7],[1,4]]
print(mergeIntervals(test3_intervals))