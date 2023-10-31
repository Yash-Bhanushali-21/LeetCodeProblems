class Solution:        
    def findArray(self, pref: List[int]) -> List[int]:
        sol = [pref[0]]
        for x in range(1,len(pref)):
            lhs= pref[x-1]
            rhs=pref[x]
            print(str(lhs) + " " + str(rhs) + " ==> " + str(lhs^rhs))
            sol.append(lhs^rhs)
        return sol
            
            
            
        
        