class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = {}
        i = res = 0
        for j, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            while count[c] > 2:
                count[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res