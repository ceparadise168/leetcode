#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        memo = [0]* (len(nums)+1)
        memo[1] = nums[0]
        memo[2] = max(nums[0], nums[1])

        for i in range(3, len(nums)+1):
            memo[i] = nums[i-1] + max(memo[i-2], memo[i-3])

        return max(memo[-1], memo[-2])
# @lc code=end
