#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        memo = [0]*n
        memo[0] = 1
        memo[1] = 2
        for i in range(2, n):
            memo[i] = memo[i-1] + memo[i-2]

        return memo[-1]
# @lc code=end
