class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None. Do not return anything, modify nums in-place instead.
        """
        zero, one, two = 0, 0, 0
        for x in nums:
            if x == 0:
                zero += 1
            elif x == 1:
                one += 1
            else:
                two += 1

       
        for i in range(len(nums)):
            if i < zero:
                nums[i] = 0
            elif i < zero + one:
                nums[i] = 1
            else:
                nums[i] = 2
