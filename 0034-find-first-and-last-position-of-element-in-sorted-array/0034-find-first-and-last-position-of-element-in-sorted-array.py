class Solution:
    def solve(self,nums : List[int], target : int) -> List[int]:
        start = 0
        end = len(nums) - 1
        solution = []
        firstOccurenceIndex = -1
        lastOccurenceIndex = -1
        while start <= end:
            mid = start + (end - start) // 2

            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                firstOccurenceIndex = mid
                break
        
        if firstOccurenceIndex != -1:
            while firstOccurenceIndex - 1 >= 0 and nums[firstOccurenceIndex - 1] == target:
                firstOccurenceIndex -= 1
        #else its confirmed its first occurence.
        lastOccurenceIndex = firstOccurenceIndex
        while lastOccurenceIndex != -1 and lastOccurenceIndex + 1 < len(nums) and nums[lastOccurenceIndex + 1] == target:
            lastOccurenceIndex += 1
       
                    
        solution.append(firstOccurenceIndex)
        solution.append(lastOccurenceIndex)
        
        return solution
                                 
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:       
        return self.solve(nums,target)