'''
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... 
forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. 
You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

Input: routes[[]], routes[i] will go through this sequence, source:int, target: int 
Output: least num of buses 

BFS:

Backtracking: 



Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
i = bus, ij = stop
dict: stop: busi, busi+1 ...
        1 : 0
        2 : 0
        7 : 0, 1
        3 : 1
        6 : 1
BFS:
    1. Build adj {}, stop# : [bus# / busidx]
    2. queue = [source], min_buses = float(inf), visited_stops = set(source), visited_busses = set()
    3. while queue:
        a. buses_taken += 1 
        pop queue, get stop list from adj
        b. new_queue = []
        c. for every stop in adj[curr]
            if stop == target:
                break & return -> reached target
            else:
                new_queue.append(stop)
        queue = new_queue
        min_busses += 1
    4.  return min busses




                


'''

def bus_routes():
    pass