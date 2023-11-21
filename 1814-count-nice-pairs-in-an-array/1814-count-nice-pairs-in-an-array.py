#nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
#we can solve this eq. as nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
class Solution:
    def rev(self,num : int) -> int:
        sign = 1 if num >= 0 else -1
        num = abs(num)
        reversed_num = 0

        while num > 0:
            reversed_num = reversed_num * 10 + num % 10
            num //= 10

        return sign * reversed_num
    
    def countNicePairs(self, nums: List[int]) -> int:

        freq = {}
        ans = 0
        
        for x in nums:
            val = x - self.rev(x)
            ans = (ans + freq.get(val, 0))%(pow(10,9) + 7)
            freq[val] =  freq.get(val, 0) + 1
  
        
        return ans%(pow(10,9) + 7)
        