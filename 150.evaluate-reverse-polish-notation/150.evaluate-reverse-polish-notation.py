#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from math import floor, ceil
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = "+-*/"
        q = []
        fisrt, second = 0, 0
        for t in tokens:
            q.append(t)
            if t in op:
                operator = q.pop()
                second = q.pop()
                first = q.pop()
                q.append(self.doOp(first, second, operator))
        return int(q.pop())
    def doOp(self, first, second, op):
        first = int(first)
        second = int(second)
        if op == '+':
            return first+second
        if op == '-':
            return first-second
        if op == '*':
            return first*second
        if op == '/':
            r = first/second
            return floor(r) if r > 0 else ceil(r)
# @lc code=end