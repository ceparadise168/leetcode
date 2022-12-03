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
        if not s: return s

        # Convert s to a list.
        s = list(s)

        # Sort the characters in s.
        s.sort()

        # Make a list of strings, one for each unique char.
        all_strings = []
        cur_sb = [s[0]]
        for c in s[1:]:
            # If the last character on string builder is different...
            if cur_sb[-1] != c:
                all_strings.append("".join(cur_sb))
                cur_sb = []
            cur_sb.append(c)
        all_strings.append("".join(cur_sb))

        # Sort the strings by length from *longest* to shortest.
        all_strings.sort(key=lambda string : len(string), reverse=True)

        # Convert to a single string to return.
        # Converting a list of strings to a string is often done
        # using this rather strange looking python idiom.
        return "".join(all_strings)
# @lc code=end

print(Solution().frequencySort(s="tree"))
print(Solution().frequencySort(s="cccaaa"))
print(Solution().frequencySort(s="Aabb"))