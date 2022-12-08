#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.dfs(root, low, high, 0)

    def dfs(self, root, low, high, s):
        if root:
            if low <= root.val <= high:
                s += root.val
            if root.left:
                s = self.dfs(root.left, low, high, s)
            if root.right:
                s = self.dfs(root.right, low, high, s)
        return s
# @lc code=end
