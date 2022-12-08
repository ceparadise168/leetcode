#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.dfs(root1, []) == self.dfs(root2, [])

    def dfs(self, root, leafs):
        if root:
            if not root.left and not root.right:
                leafs.append(root.val)
            if root.left:
                self.dfs(root.left, leafs)
            if root.right:
                self.dfs(root.right, leafs)
        return leafs

# @lc code=end
