class Solution:
    def first(self,arr, low, high, key, length):
        if key in arr:
            return arr.index(key)
        return -1
      
 
    def last(self,arr, low, high, key, length): 
        if key in arr:
            return length - 1 - arr[::-1].index(key)
        return -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        solution = []
        firstOccurence = self.first(nums,0, n - 1,target, n)
        secondOccurence = self.last(nums,0, n - 1,target, n)
        solution.append(firstOccurence)
        solution.append(secondOccurence)
        return solution