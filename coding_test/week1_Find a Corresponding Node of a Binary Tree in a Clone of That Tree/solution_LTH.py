# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        ans = self.dfs(cloned, target)
        
        return ans
        
    def dfs(self, tree, target):
        if not tree:
            return False
        
        if tree.val == target.val:
            return tree
        
        left = self.dfs(tree.left, target)
        right = self.dfs(tree.right, target)

        return left or right