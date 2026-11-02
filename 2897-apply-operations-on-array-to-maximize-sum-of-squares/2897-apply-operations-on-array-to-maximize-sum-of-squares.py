class Solution:
     def maxSum(self, A: List[int], k: int) -> int:
        count = [0] * 35
        for a in A:
            for i in range(35):
                if a & (1 << i):
                    count[i] += 1
        res = 0
        mod = 10 ** 9 + 7
        for j in range(k):
            cur = 0
            for i in range(35):
                if count[i]:
                    count[i] -= 1
                    cur += 1 << i
            res += cur * cur % mod
        return res % mod