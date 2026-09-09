class Solution:
    def countCommas(self, n: int) -> int:
        curr=1000
        ctr=0
        while n >=curr:
            ctr+=(n-curr+1)
            curr*=1000
        return ctr