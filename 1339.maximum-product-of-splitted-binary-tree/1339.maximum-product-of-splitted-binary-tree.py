#
# @lc app=leetcode id=1339 lang=python3
#
# [1339] Maximum Product of Splitted Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        all_sums = []

        def getTreeSum(root):
            if not root:
                return 0
            left_sum = getTreeSum(root.left)
            right_sum = getTreeSum(root.right)
            total_sum = root.val + left_sum + right_sum
            all_sums.append(total_sum)
            return total_sum

        total_sum = getTreeSum(root)

        max_product = 0
        for sub_tree_sum in all_sums:
            max_product = max(max_product, sub_tree_sum*(total_sum-sub_tree_sum))
        return max_product % (10**9 + 7)
# @lc code=end
