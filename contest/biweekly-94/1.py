class Solution:
    def captureForts(self, forts: List[int]) -> int:
        l, r = 0, 0
        cnt = 0
        while l < len(forts) - 2:
            if forts[l] == 1:
                temp_cnt = 0
                r = l+1
                for r in range(r, len(forts)):
                    if forts[r] == 0:
                        temp_cnt += 1
                    elif forts[r] == -1:
                        cnt = max(cnt, temp_cnt)
                        break
                    else:
                        break
                l = r
            else:
                l += 1

        forts = forts[::-1]
        l, r = 0, 0
        while l < len(forts) - 2:
            if forts[l] == 1:
                temp_cnt = 0
                r = l+1
                for r in range(r, len(forts)):
                    if forts[r] == 0:
                        temp_cnt += 1
                    elif forts[r] == -1:
                        cnt = max(cnt, temp_cnt)
                        break
                    else:
                        break
                l = r
            else:
                l += 1
        return cnt