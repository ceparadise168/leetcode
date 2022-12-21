#
# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#

# @lc code=start
from collections import defaultdict
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        memo = defaultdict(set)

        for a, b in dislikes:
            memo[a].add(b)
            memo[b].add(a)

        color = dict()
        for i in range(1, n+1):
            if i not in color:
                q = [i]
                color[i] = 1
                while q:
                    a = q.pop()

                    for b in memo[a]:
                        if b not in color:
                            color[b] = -1*color[a]
                            q.append(b)
                        else:
                            if color[b] == color[a]:
                                return False
        return True
# @lc code=end
