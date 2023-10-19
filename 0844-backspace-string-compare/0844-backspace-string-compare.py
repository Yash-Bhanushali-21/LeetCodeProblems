class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stringS = ""
        stringT = ""
        for x in s:
            if x == "#":
                stringS = stringS[:-1]
            else:
                stringS += x
        for x in t:
            if x == "#":
                stringT = stringT[:-1]
            else:
                stringT += x
        
        return stringS == stringT
        