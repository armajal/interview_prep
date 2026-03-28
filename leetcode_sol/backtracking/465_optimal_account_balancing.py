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
    
    debtss = [v for v in balance.values() if v!= -]
    


    backtracking(i):
        while i < len(debts) and debts[i] != 0:
            i +=1  # skip settled

        if i == len(debts)
            return 0 # everybody is settles 
        
        # Choose = modify settle map and do transaction
        for j in range(i + 1, len(debts)):
            if debts[j] * debts[i] < 0:
                debtspj
 += debts[i]
            min_count = min(min_count, 1+ backtracking(i + 1))
        
        reeturn min_count
    return backtracking(0)

    

        



        



    
    





'''