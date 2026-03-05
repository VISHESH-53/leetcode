class Solution:
    def minOperations(self, s):
        cnt = 0
        n = len(s)
        for i, char in enumerate(s):
            if i % 2 == 0:
                if char != '0':
                    cnt += 1
            else:
                if char != '1':
                    cnt += 1
        return min(cnt, n - cnt)
