#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_idx = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= last_idx:
                last_idx = i

        return last_idx == 0

# @lc code=end
