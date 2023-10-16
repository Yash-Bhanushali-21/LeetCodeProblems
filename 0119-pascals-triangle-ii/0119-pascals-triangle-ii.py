class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        
        previousRow = self.getRow(rowIndex - 1)
        currentRow = [1]
        
        for i in range(1, rowIndex):
            currentRow.append(previousRow[i] + previousRow[i - 1])
            
        currentRow.append(1)
        
        return currentRow