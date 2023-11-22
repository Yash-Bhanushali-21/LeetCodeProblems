class Solution:
    def findMaxColumnLen(self,nums : List[List[int]]) -> int:
        maxLength = 0
        for row in range(0,len(nums)):
            maxLength = max(len(nums[row]),maxLength)
        return maxLength
    
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        solution = []
        d = {}
        maxSum = 0
        for i in range(len(nums) - 1, -1, -1):
            for j, val in enumerate(nums[i]):
                diagonal_index_sum = i + j
                maxSum = max(diagonal_index_sum,maxSum)
                if diagonal_index_sum not in d:
                    d[diagonal_index_sum] = []
                d[diagonal_index_sum].append(val)
                
        for i in range(0,maxSum + 1):
            for element in d[i]:
                solution.append(element)
                
        return solution
                
        