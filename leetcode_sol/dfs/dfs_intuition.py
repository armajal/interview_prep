'''
1. Base Case, simplest possible 
2. Do you want to do business logic for children or root
3. Do you need a global state? 

---------------
Recusion

1. Get a base case, the simplest problem 
2. Play around and visualize
3. Relate hard cases to simpler cases
4. Generalize the pattern
5. Write the recursive statement combining base case

'''

# Ex. Write a fx that counts num of ways you can partion n objects using parts up to m (assuming m>= 0)
'''

1. Write the base casee
 obj = 1, 1partition
 obj = 0, 1 partition
 1 if n = 0
 0 if m = 0


2. Play around with cases n
    n = 2: **, * + *                   = 2
    n = 3; ** + *, ****, * + **       = 3
    n = 5:  = **** + *, *****, *** + **, ** + * + * + *, ** + ** + *, * + * + * + * + *, ** + * + * + * = 7
    n = 6: = ******, ***** + *, *** + ** + *, ** + * + ** + *, ** + * + * + * + *, * + * + * + * + * + * = 9
3. Relate to smaller
count_partitions(n, m-1) is a subset of count_partitions(n, m)
count_partitions(n - m, m) are what is left

4. Generalize the patterns
 count_partitions(n, m) = 1 if n = 0 
                          0 if m = 0
        what if n < m?    0 if m < = 0

                        = count_partitions(n, m-1) + count_partitions(n - m, m)
'''


#5 Writee code combining recurrsive cases and base case    
def count_partitions(n: int, m: int):
    if n == 0:
        return 1
    
    if m <= 0:
        return 0
    
    else:
        return count_partitions(n, m-1) + count_partitions(n - m, m)