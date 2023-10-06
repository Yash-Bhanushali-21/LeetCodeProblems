class Solution:
    def solve(self, solution : int, k : int, n : int, memo) -> int:
        if k >= 2 and n == 0:
            return solution
        
        elif k >= 2 and n < 0:
            return -1
        
        if (solution,n) in memo:
            return memo[(solution,n)]
        
            
        res = 0
        
        for x in range(1,n + 1):
            recur = self.solve(solution * x ,k + 1, n - x,memo)
            res = max(res, recur)
            
        memo[(solution,n)] = res
        
        return res
            
        
    def integerBreak(self, n: int) -> int:
        memo = {}
        return self.solve(1, 0 , n, memo)
        
        
        
        