class Solution:
    def largestOddNumber(self, num: str) -> str:
        startPointer = 0
        endPointer = -1
        
        if int(num[len(num) - 1]) % 2 != 0:
            return num

        for rightPointer in range(len(num) - 1, -1,-1):
            if int(num[rightPointer]) % 2 != 0:
                endPointer = rightPointer
                break
            
        if endPointer == -1:
            return ""
    
        return num[startPointer:endPointer + 1]