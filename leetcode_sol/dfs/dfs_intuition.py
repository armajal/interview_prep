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

'''
Number of Islands: given m x n grid represents 1s (land) and 0s (water), return num of islands
    Island: surrounded by water or land is horizontal or vertical. Edges are surrounded by watter

1. Start with simple base case
1 if m = 0 or n = 0
1 if m = edge or n = edge

2. Play w/ examples
1 1 0  3 islands            0 1 1 1 0 0 0
0 0 1                       0 1 0 0 0 0 0 4 islands
1 0 1                       1 0 0 0 1 0 1

3. Relate to harder cases

    
4. Geneeralize
    sum = 0
   for i, j in mxn
    if grid[i][j] == 1
        dfs
            if grid[i][j] != 1 and i or j < 0 or i, j > m-1, n-1
                return 0
          grid[i][j] = 0, setting as visited
          go dfs(horizontal) and dfs vertical
        sum += 1

5. Code




'''
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    num_islands += 1

        return num_islands

    def dfs(self, grid, r, c):
        if (
            r < 0
            or c < 0
            or r >= len(grid)
            or c >= len(grid[0])
            or grid[r][c] != "1"
        ):
            return
        grid[r][c] = "0"

        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)