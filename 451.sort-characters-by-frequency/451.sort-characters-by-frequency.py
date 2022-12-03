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
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start

class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        ans = ''
        items = sorted(c.items(), key=lambda pair: pair[1], reverse=True)
        for char, feq in items:
            ans += char*feq
        return ans
# @lc code=end

print(Solution().frequencySort(s="tree"))
print(Solution().frequencySort(s="cccaaa"))
print(Solution().frequencySort(s="Aabb"))