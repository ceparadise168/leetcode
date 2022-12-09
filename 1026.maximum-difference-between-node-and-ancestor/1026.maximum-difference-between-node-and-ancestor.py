#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, root.val, root.val, 0)

    def dfs(self, root, minAncestor, maxAncestor, maxDiff):
        if root:
            maxDiff = max(maxDiff, abs(minAncestor-root.val),  abs(maxAncestor-root.val))
            minAncestor = min(minAncestor, root.val)
            maxAncestor = max(maxAncestor, root.val)
            if root.left:
                maxDiff = self.dfs(root.left, minAncestor, maxAncestor, maxDiff)
            if root.right:
                maxDiff = self.dfs(root.right, minAncestor, maxAncestor, maxDiff)

        return maxDiff
# @lc code=end
