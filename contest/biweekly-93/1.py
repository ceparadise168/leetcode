import re

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maxLen = 0

        for s in strs:
            if re.search('[a-zA-Z]', s):
                maxLen = max(maxLen, len(s))
            else:
                maxLen = max(maxLen, int(s))
        return maxLen