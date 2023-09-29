class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        increasing = decreasing = True

        for index in range(len(nums) - 1):
            if nums[index] > nums[index + 1]:
                increasing = False
            elif nums[index] < nums[index + 1]:
                decreasing = False
            elif increasing == False and decreasing == False:
                break

        return increasing or decreasing
        