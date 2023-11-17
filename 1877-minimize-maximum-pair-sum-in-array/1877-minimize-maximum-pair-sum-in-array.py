class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        max_value = 0
        nums.sort()
        i,j = 0 , len(nums) - 1
        while i < j:
            max_value = max(nums[i] + nums[j], max_value)
            i+=1
            j-=1
        return max_value
        
        