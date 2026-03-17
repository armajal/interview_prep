'''
3:57pm
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]

-------------------------
Input: 0, numCourses-1, preRequisite[] = [course, preRequisite]
Output: Order of courses or empty array
Constraint: return order of courses to take 
Tool: Topological Sort 

3:58pm
Approach:
    indegree, course_order, = []
    adj_list = dict()
    queue = deque

    1. create indegree
    for course_pair in prerequisites[]:
        
    
    2. topological sort

'''
from collections import deque
from collections import defaultdict
# 4:05PM 
def course_schedule_finder(numCourses: int, prerequisites: list[list[int]]) -> [int]:
    indegree = [0] * numCourses
    order = []
    adj_list = defaultdict(list)
    queue = deque()
    
    for course_pair in prerequisites:
        pre = course_pair[1]
        course = course_pair[0]
        adj_list.setdefault(course, [])
        adj_list.setdefault(pre, []).append(course)
        indegree[course] += 1

    
    for course in range(len(indegree)):
        if indegree[course] == 0:
            queue.append(course)

    while queue:
        curr = queue.popleft()
        order.append(curr)

        for course in adj_list[curr]:
            indegree[course] -= 1
            if indegree[course] == 0:
                queue.append(course)


    return order if len(order) == numCourses else []

# Testing 4:16 pm 
numCourses = 2
prerequisites = [[1,0]]
print("Output:", course_schedule_finder(numCourses, prerequisites))
# Expected Output: [0,1] Finished 4:28, Wrong Direction of appending 

# Passed with [0,1,2,3]
numCourses2 = 4
prerequisites2 = [[1,0],[2,0],[3,1],[3,2]]
print("Output 2:", course_schedule_finder(numCourses2, prerequisites2))
# Expected Output: [0,2,1,3]

# Passed at 4:32pm 
numCourses3 = 1
prerequisites3 = []
print("Output 3:", course_schedule_finder(numCourses3, prerequisites3))
# Expected Output: Output: [0]