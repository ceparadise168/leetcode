#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
from collections import defaultdict
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        memo = defaultdict(set)

        for idx, keys in enumerate(rooms):
            memo[idx] = set(keys)

        q = []

        start = 0
        keys = list(memo[start])
        used_keys = memo[start]
        while keys:
            key = keys.pop(0)
            keys_of_room = memo[key]

            for k in keys_of_room:
                if k not in used_keys and k != 0:
                    keys.append(k)
                    used_keys.add(k)

        return len(used_keys) == len(rooms) - 1
# @lc code=end
