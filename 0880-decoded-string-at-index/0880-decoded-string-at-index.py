class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for c in s:
            if c.isdigit():
                size *= int(c)
            else:
                size+=1
        for i in reversed(range(0, len(s))):
            k %= size
            
            if k==0 and s[i].isdigit() == False:
                return s[i]
            
            if s[i].isdigit():
                size //= int(s[i])
            else:
                size-=1
            
        return ""
        
                    
                
                
                
            
        