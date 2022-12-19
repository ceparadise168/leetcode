#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#
from collections import defaultdict
# @lc code=start
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        paths = defaultdict(set)
        for edge in edges:
            u, v = edge
            paths[u].add(v)
            paths[v].add(u)

        q = [source]
        visited = set()
        visited.add(source)
        while q:
            node = q.pop(0)
            if node == destination:
                return True
            for n in paths[node]:
                if n not in visited:
                    q.append(n)
                    visited.add(n)
        return False

# @lc code=end
