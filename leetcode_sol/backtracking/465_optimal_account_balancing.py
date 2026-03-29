'''
You are given an array of transactions transactions where transactions[i] = 
[fromi, toi, amounti] indicates that the person with ID = fromi gave amounti $ to the person with ID = toi.

Return the minimum number of transactions required to settle the debt.


Input: transactionss [], from -> to : amount
Output: min num of transactions to settle debt

Examples:
A.   transactions = [[0,1,10],[2,0,5]]   
        0 -> 5
        1 -> 10
        2
    Output 2: 

B.  transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
    0 -> 6
    1 -> 10
    2 -> 5



algo: 
    min_count = float(-'inf')
    n = len(transactions) 
    adj = {people, amount}

    for frm, to, amt in transactions:
        adj[from] -= amt
        adj[to] += amt
    
    debtss = [v for v in balance.values() if v!= 0]
    
    backtracking(i):
        while i < len(debts) and debts[i] == 0:
            i +=1  # skip settled

        if i == len(debts)
            return 0 # everybody is settles 
        
        # Choose = modify settle map and do transaction
        for j in range(i + 1, len(debts)):
            if debts[j] * debts[i] < 0:
                debts[j] += debts[i]
                min_count = min(min_count, 1 + backtracking(i + 1)) 
                debts[j] -= debts[i]
        
        reeturn min_count
    return backtracking(0)

'''

def settleTransactions(transactions: list[list[int]]) -> int:
    adj = {}

    for t in transactions:
        from_i = t[0]
        to_i = t[1]
        amt = t[2]
        adj[from_i] = adj.setdefault(from_i, 0) - amt
        adj[to_i] = adj.setdefault(to_i, 0) + amt

    debts = [adj[p] for p in adj.keys() if adj[p] != 0]
    
   
    n = len(debts)
    def backtracking(i):
        while i < n and debts[i] == 0: # If the debts are settled, skip this iterations
            i += 1

        if i == n:
            return 0 # Got to the end of the debts
        
        min_amount = float('inf')
        for j in range(i +1, n):
            if debts[j] * debts[i] < 0: # - * + = - which means there is a debt
                debts[j] += debts[i]
                min_amount = min(min_amount, 1 + backtracking(i + 1))
                debts[j] -= debts[i] # Classic backtracking undo

        return min_amount

    
    return backtracking(0)

test_transactions = [[0,1,10],[2,0,5]]
print(settleTransactions(test_transactions))