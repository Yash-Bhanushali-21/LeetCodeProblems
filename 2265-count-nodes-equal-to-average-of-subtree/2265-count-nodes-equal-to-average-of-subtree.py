# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, root, nodeAttribute):
        if root is None:
            return {"count": 0, "sumNodes": 0 ,"solution" : 0 } 
        
       
        leftSubTree = self.solve(root.left, nodeAttribute)
        rightSubTree = self.solve(root.right, nodeAttribute)

        leftSubTreeCount = leftSubTree["count"]
        leftSubTreeSum = leftSubTree["sumNodes"]

        rightSubTreeCount = rightSubTree["count"]
        rightSubTreeSum = rightSubTree["sumNodes"]

        currentNodeAverage = (root.val + rightSubTreeSum + leftSubTreeSum) // (1 + leftSubTreeCount + rightSubTreeCount)

        
        solutionNodeCount = leftSubTree["solution"] + rightSubTree["solution"]
        
        updatedDict= {
            "count": 1 + leftSubTreeCount + rightSubTreeCount,
            "sumNodes": root.val + rightSubTreeSum + leftSubTreeSum,
            "solution" : solutionNodeCount + 1 if currentNodeAverage == root.val else solutionNodeCount
        
        }
        

        return updatedDict

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        tempDictForDummyNode = {"node" : -1 ,"count": 0, "sumNodes": 0, "solution" : 0}
        solutionDict=self.solve(root, tempDictForDummyNode)
        return solutionDict["solution"]
        
        return 0  