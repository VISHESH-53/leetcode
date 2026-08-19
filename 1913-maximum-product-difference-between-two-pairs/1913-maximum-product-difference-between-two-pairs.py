class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        l=nums
        a=max(l)
        d=min(l)
        l.remove(a)
        l.remove(d)
        b=max(l)
        c=min(l)
        return ((a*b)-(c*d))
