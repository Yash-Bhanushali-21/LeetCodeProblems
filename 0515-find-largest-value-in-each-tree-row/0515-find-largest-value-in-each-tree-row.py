import sys

class Solution:
    def height(self,node):
        if node is None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1
    
    def getMaxValueForCurrentLevel(self,root, level,maximumValue):
        if root is None:
            return maximumValue  
        if level == 1:
            maximumValue = max(maximumValue, root.val)
        elif level > 1:
            maximumValue = self.getMaxValueForCurrentLevel(root.left, level-1,maximumValue)
            maximumValue = self.getMaxValueForCurrentLevel(root.right, level-1,maximumValue)
        return maximumValue  
            
            
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        h = self.height(root)
        maximumValues = []
        
        for i in range(1, h+1):
            maximumValue = -sys.maxsize
            maximumValue = self.getMaxValueForCurrentLevel(root, i, maximumValue)
            maximumValues.append(maximumValue)
        
        return maximumValues

       