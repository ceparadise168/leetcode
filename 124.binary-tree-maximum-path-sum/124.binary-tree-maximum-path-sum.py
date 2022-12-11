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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = -float('inf')

        def max_path_sum_of_subtree(root) -> int:
            nonlocal max_path

            if not root:
                return 0

            max_left_path_sum = max(max_path_sum_of_subtree(root.left), 0)
            max_right_path_sum = max(max_path_sum_of_subtree(root.right), 0)
            max_path = max(max_path, max_left_path_sum + max_right_path_sum + root.val)

            return max(max_left_path_sum + root.val, max_right_path_sum + root.val)

        max_path_sum_of_subtree(root)

        return max_path