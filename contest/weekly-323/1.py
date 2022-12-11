class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        sgrid = []

        for g in grid:
            sgrid.append(sorted(g))

        rm_nums = []
        while sgrid:
            maxNum = 0
            for g in sgrid:
                maxNum = max(maxNum, g.pop())
            rm_nums.append(maxNum)
            if not sgrid[0]:
                break

        return sum(rm_nums)