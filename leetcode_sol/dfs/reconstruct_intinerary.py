'''
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. 
Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, 
you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example 1:


Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
Example 2:


---------
DFS with reverse sort to get last. 
    Build from leave-> root it is a post order
    Post order because we need to know when an airport has been reached 

    ex:
        jfk      sfo     sjc    muc       
        at each queue, lexicaly order /sort  it 
    
    
'''
from collections import deque
def find_multiple_intinerary(tickets: [str])-> list[str]:
    adj_map = {}

    for from_i, to_i in sorted(tickets, reverse=True):
        adj_map.setdefault(from_i, []).append(to_i)
        adj_map.setdefault(to_i, [])

    res = []
    
    def dfs(airport):
        while adj_map[airport]:
            next_airport = adj_map[airport].pop()
            dfs(next_airport)
        res.append(airport)

    dfs("JFK")
    print(res)
    print("reverse?", res[::-1])
    return res[::-1]

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
print(find_multiple_intinerary(tickets))
#Output: ["JFK","MUC","LHR","SFO","SJC"]
