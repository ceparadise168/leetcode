class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        max_len = -1
        nums.sort()
        s = set(nums)

        for n in nums:
            r = n
            for i in range(2, len(nums)+1):
                r *= r
                if r in s:
                    max_len = max(max_len, i)
                else:
                    break
        return max_len
        # max_len = -1
        # ones = nums.count(1)
        # if ones > 1:
        #     max_len = ones

        # nums = set(nums)

        # check = list(nums)
        # check.sort()

        # while nums:
        #     num = check.pop(0)
        #     nums.discard(num)
        #     if num == 1:
        #         nums.discard(1)
        #         continue

        #     curr = 1
        #     sq = num**2
        #     while sq in nums:
        #         nums.discard(sq)
        #         sq = sq**2
        #         curr += 1
        #     if curr > 1:
        #         max_len = max(max_len, curr)
        # return max_len