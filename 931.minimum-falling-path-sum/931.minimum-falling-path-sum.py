#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rl = len(matrix)
        cl = len(matrix[0])

        memo = dict()

        def pathSum(r, c):
            if not (0 <= c < cl):
                return float('Inf')

            if r == rl-1:
                return matrix[r][c]

            # optimize
            if (r+1, c-1) in memo:
                left = memo[(r+1, c-1)]
            else:
                left = pathSum(r+1, c-1)
                memo[(r+1, c-1)] = left

            if (r+1, c) in memo:
                mid = memo[(r+1, c)]
            else:
                mid = pathSum(r+1, c)
                memo[(r+1, c)] = mid

            if (r+1, c+1) in memo:
                right = memo[(r+1, c+1)]
            else:
                right = pathSum(r+1, c+1)
                memo[(r+1, c+1)] = right

            return  min(left, mid, right) + matrix[r][c]

            # Time Limit Exceeded
            # return min(
            #     matrix[r][c] + pathSum(r+1, c-1),
            #     matrix[r][c] + pathSum(r+1, c),
            #     matrix[r][c] + pathSum(r+1, c+1)
            # )

        minPathSum = float('Inf')
        for i in range(len(matrix[0])):
            minPathSum = min(minPathSum, pathSum(0, i))

        return int(minPathSum)
# @lc code=end
