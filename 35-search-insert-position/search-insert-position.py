class Solution(object):
    def bs(self, l, arr, h, x):
        if l > h:
            return l

        mid = (l + h) // 2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return self.bs(mid + 1, arr, h, x)
        else:
            return self.bs(l, arr, mid - 1, x)

    def searchInsert(self, nums, target):
        return self.bs(0, nums, len(nums) - 1, target)
