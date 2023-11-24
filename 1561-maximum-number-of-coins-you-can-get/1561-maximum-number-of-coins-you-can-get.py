from itertools import combinations

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        s = 0
        for i in range(len(piles) //3 , len(piles) , 2):
            s += piles[i]
        return s
            
        