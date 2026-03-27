'''
Given an array of meeting time intervals intervals where 
intervals[i] = [starti, endi], return the minimum number of
 conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1

'''
import heapq
def meeting_rooms(intervals : list[list[int]]) -> list[list[int]]:
    new_intvs = sorted(intervals, key=lambda intv: intv[0])

    heap = [new_intvs[0][1]]
    heapq.heapify(heap)
    
    for intv in range(1, len(new_intvs)):
        start = new_intvs[intv][0]
        end = new_intvs[intv][1]

        if heap and heap[0] <= start: # If intv's start is outsidee of last end time 
            heapq.heappop(heap) # remove to make space for free room
        
        heapq.heappush(heap, end)
    return len(heap)

intervals = [[0,30],[5,10],[15,20]]
print(meeting_rooms(intervals))


intervals2 = [[7,10],[2,4]]
print(meeting_rooms(intervals2))
        

