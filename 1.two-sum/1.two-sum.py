from typing import List
import collections
import itertools
import functools
import math
import string
import random
import bisect
import re
import operator
import heapq
import queue

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()
        for idx, num in enumerate(nums):
            need = target - num
            if need in m:
                return [m[need], idx]
            m[num] = idx
        return [-1, -1]
# @lc code=end
print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
print(Solution().twoSum(nums=[2, 7, 11, 15], target=18))
print(Solution().twoSum(nums=[2, 7, 11, 15], target=22))