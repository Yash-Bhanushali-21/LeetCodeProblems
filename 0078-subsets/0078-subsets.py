class Solution:
    def solve(self,nums:List[int],index : int, currentSol : List[int],sol : List[List[int]]):
        sol.append(currentSol[:])
        
        for i in range(index,len(nums)):
            currentSol.append(nums[i])
            self.solve(nums,i + 1, currentSol,sol)
            currentSol.pop()
         
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currentSol =  []
        solution = []
        self.solve(nums,0,currentSol, solution)
        return solution
    
        