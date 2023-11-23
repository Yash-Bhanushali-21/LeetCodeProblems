class Solution:
    def has_same_difference(self,arr):
        if len(arr) < 2:
            return True
        
        common_difference = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != common_difference:
                return False
        return True

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            current_arr = nums[l[i]:r[i]+1]
            current_arr.sort()
            res.append(self.has_same_difference(current_arr))
        return res