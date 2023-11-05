class Solution:
    def solve(self,m : int,n: int,r: int,d: int,memo : dict) -> int:
            if r > m - 1 or d > n - 1:
                return 0
            elif r == m - 1 and d == n - 1:
                return 1
            elif (r,d) in memo:
                return memo[(r,d)]
            memo[(r,d)] = self.solve(m,n,r+1,d,memo) + self.solve(m,n,r,d+1,memo)
            
            return memo[(r,d)]
    
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        return self.solve(m,n,0,0,memo)
        
        