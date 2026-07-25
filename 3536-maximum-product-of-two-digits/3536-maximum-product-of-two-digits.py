class Solution:
    def maxProduct(self, n: int) -> int:
        l = [int(x) for x in str(n)]
        l.sort()
        return l[-1]*l[-2]
        