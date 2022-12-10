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

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        if len(edges) == 0:
            return max(vals)

        conn_counts = defaultdict(list)

        for edge in edges:
            if vals[edge[1]] > 0:
                conn_counts[edge[0]].append(vals[edge[1]])
            if vals[edge[0]] > 0:
                conn_counts[edge[1]].append(vals[edge[0]])

        output = max(vals)
        for start_node, conn_node_vals in conn_counts.items():
            conn_node_vals.sort(reverse = True)

            s = vals[start_node]
            for i in range(min(k, len(conn_node_vals))):
                if conn_node_vals[i] > 0:
                    s+=conn_node_vals[i]
                else:
                    break
            output = max(output, s)

        return output