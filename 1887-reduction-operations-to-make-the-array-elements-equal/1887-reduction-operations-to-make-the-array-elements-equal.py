class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        previous = nums[0]
        for x in range(1,len(nums)):
            if previous != nums[x]:
                count += len(nums) - x
                previous = nums[x]
        return count