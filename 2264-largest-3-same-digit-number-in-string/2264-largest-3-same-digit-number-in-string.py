class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        solution = -1
        for slidingWindowIndex in range(0,n):
            if slidingWindowIndex + 2 < n:
                itemAtFirstIndex = num[slidingWindowIndex]*3
                if itemAtFirstIndex == num[slidingWindowIndex : slidingWindowIndex + 3]:
                    solution = max(int(solution),int(itemAtFirstIndex))
        if solution == 0:
            return "000"
        if solution == -1:
            return ""
        return str(solution)
                    
                
        