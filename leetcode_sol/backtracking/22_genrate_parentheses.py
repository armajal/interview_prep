'''
Given n pairs of parentheses, 
write a function to generate all combinations of well-formed parentheses.

Input: number of parenthesis 
Output: combinations of proper parenthesis 

Examples:
    1 = ()
    2 = () (), (())
    3 = () () (), () (()), (()) (), ((())), 

    Chose:
        Put new set of parenthesis
            1. Add ()
            2. Wrap Around each existing options
            path: (()) -> ((())), (()) ()

    Don't 
        Don't put a new set in there
    
    Constraints:
        If i == n 
'''
def generateParenthesis(n: int) -> list[str]:
    parenPair = ["(", ")"]

    res = []

    def dfs(path, left, right):
        # Base Case
        if len(path) == 2 * n:
            res.append("".join(path))
            return

        # Choice
        if left < n:
            path.append("(")
            dfs(path, left + 1, right)
            path.pop()

        if right < left:
            path.append(")")
            dfs(path, left, right + 1)
            path.pop()
        

    dfs([], 0, 0)
    return res

print(generateParenthesis(1))

print(generateParenthesis(3))

