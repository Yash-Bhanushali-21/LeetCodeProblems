# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, d):
        if root is None:
            return
        d[root.val] += 1
        self.traverse(root.left, d)
        self.traverse(root.right, d)
        
    def findMode(self, root):
        if not root:
            return []
        
        d = defaultdict(int)
        self.traverse(root, d)
        
        max_freq = max(d.values())
        result = [key for key, value in d.items() if value == max_freq]
        return result
                
        