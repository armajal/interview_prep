class union_find:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def add(self, x:int):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def union(self, x, y):
        '''
        # Base Case:
        root_x = self.find(x)
        root_y = self.find(y)
        parent[root_x] = root_y
        '''
        # Path Compression
        root_x, root_y = self.find(x), self.find(y)
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y

        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        
        else: 
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
    
    def find(self, x:int) -> int:
        '''
        # Base Case:
        while self.parent[x] != x:
            x = self.parent[x]
        return x
        '''

        # Path Compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]