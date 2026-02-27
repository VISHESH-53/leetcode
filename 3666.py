
class Solution(object):
    def ceil(self, x, y):
        return (x + y - 1) // y

    def minOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        z = s.count("0")
        if n == k:
            if z == 0:
                return 0
            elif z == n:
                return 1
            else:
                return -1

        inf = float('inf')
        ans = inf
        if z % 2 == 0:
            m = max(self.ceil(z, k), self.ceil(z, n - k))
            m += m & 1
            ans = min(ans, m)

        if z % 2 == k % 2:
            m = max(self.ceil(z, k), self.ceil(n - z, n - k))
            m += (m & 1) == 0
            ans = min(ans, m)
            
        return ans if ans < inf else -1
