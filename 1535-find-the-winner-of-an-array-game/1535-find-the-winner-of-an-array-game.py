class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = arr[0]
        consecutiveWinnerCount = 0
        
        for x in range(1,len(arr)):
            if winner > arr[x]:
                consecutiveWinnerCount += 1
            elif winner < arr[x]:
                winner = arr[x]
                consecutiveWinnerCount = 1
            
            if consecutiveWinnerCount == k:
                return winner
        return winner