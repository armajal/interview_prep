'''
You are given an array of variable pairs equations and an array of real numbers values, 
where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

--------------------
Input: equations[], values[], queries[]
Output: [] : solutions to queries 
Constraint: Find a relationship between query numerate/denominator from equations and values. 
Intuition:
    1. BFS
        Find shortest path each value in equation has relationship/ adjacency list

    2. Union Find
        Find a part of the query 

Appraoch:
    BFS:
        1. Build adj list from numerator, denominator equations[i]
            for i in idx(enumerate, equations):
                adj_list[numerator] . append((denominator, value[i]))
                adj_list[denominator]. append(numerator, 1/value[i])
        
        2. For query in Query, BFS Search
            res .append( query_response = if bfs(query) else -1 )
        
        return res

Edge Cases:
    - no zero integer division
    - if num == denom == 1 
Test Cases:
    equations [[a, b], [c, d], [d, b]], values = [2, 3, 1] queries = [[d,b], [a,d]]  | expect = [.5, -1]
        
'''

def evaluate_division(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:

    # 1. Build Adj List
    adj_list = {}
    for idx, equation in enumerate(equations):
        numerator = equation[0]
        denominator = equation[1]

        value = values[idx]

        adj_list.setdefault(numerator, []).append((denominator, value))
        adj_list.setdefault(denominator, []).append((numerator, 1/value))

    
    # 2. BFS Search
    res = []

    for query in queries:
        search_num = query[0]
        search_denom = query[1]

        
        if search_num not in adj_list or search_denom not in adj_list:
            res.append(-1.0)
            continue
        
        if search_num == search_denom:
            res.append(1.0)
            continue

        queue = [(search_num, 1.0)]
        visited = set()
        found =-1.0

        while queue:
            curr_num, curr_product = queue.pop(0)
            visited.add(curr_num)

            for neighbor, weight in adj_list[curr_num]:
                if neighbor == search_denom:
                    found = curr_product * weight
                    queue = []
                    break
                
                if neighbor not in visited:
                    queue.append((neighbor, curr_product * weight))

        res.append(found)


    return res

                    
equations_lst = [['a', 'b'], ['c', 'd'], ['d', 'b']]
values_lst = [2, 3, 1]
queries_lst = [['c','b'], ['d', 'a']]
print(evaluate_division(equations_lst, values_lst, queries_lst))



