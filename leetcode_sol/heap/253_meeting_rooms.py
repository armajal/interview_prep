'''
Start 10:52am 

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.


Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1

------------------------------

Input: array of time intervals 
Output: int, min number of conference rooms needed
Constraint: Must ordder intervals by start time to understand
Tool: Sort + Heap

Approach:
    heap = []
    1. Sort meeting_times[0][i] (start time)
    2. heap = meeting_times[0]
    3. for intv in 1, sorted meeting_times
        if heap's end is < = meeting_times[idx]: # Not overlapping, free room
            heap.pop
        else:
            push intv unto heap
    4 return len(heap)

'''
#10:55 am 
import heapq
def meeting_rooms(meeting_times: list[list[int]]) -> int:

    # 1. Sort meeting_times[0][i] (start time)
    sorted_meetings = sorted(meeting_times, key=lambda meeting_intv: meeting_intv[0])

    #2. heap = meeting_times[0]
    heap = [sorted_meetings[0][1]]
    heapq.heapify(heap)

    '''
    3. for idx intv in 1, sorted meeting_times
        if heaps's end is < meeting_times[idx]: # Overlapping, merge to create
            pop off heap
        else:
           push heap
    '''
    for intv in range(1, len(sorted_meetings)):
        start = sorted_meetings[intv][0]
        end = sorted_meetings[intv][1]

        if heap and heap[0] <= start:
            heapq.heappop(heap)
        
        heapq.heappush(heap, end)
    #4 
    return len(heap)

# Test 1 11:08 am Passed Immediately 
intervals = [[0,30],[5,10],[15,20]]
print(meeting_rooms(intervals))

# Testt 2: 11:09 am Passed Immediately 
intervals2 = [[7,10],[2,4]]
print(meeting_rooms(intervals2))

# Test3 from Leetcode failed:
# Passed by changing from stack to heap -> Misunderstood problem 
intervals3 = [[5,8],[6,8]]
print(meeting_rooms(intervals3))

'''
Reflection:
Received this in an interview, I needed a heap. I need to do concurrent how many are going at the same time. 
Here you need a heap so you can understand what frees up first, the meeting with the smallest end time will always free up first. 
 Versus a stack you care about the last meeting, the order of insertion.

'''
