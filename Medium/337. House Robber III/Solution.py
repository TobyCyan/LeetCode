from functools import cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode | None) -> int:
        
        @cache
        def dfs(node, robbing):
            if not node:
                return 0

            if robbing:
                rob = node.val + dfs(node.left, not robbing) + dfs(node.right, not robbing)
                notRob = dfs(node.left, robbing) + dfs(node.right, robbing)
                return max(rob, notRob)
            else:
                proceedLeft = dfs(node.left, not robbing)
                proceedRight = dfs(node.right, not robbing)
                return proceedLeft + proceedRight
        
        return dfs(root, True)
