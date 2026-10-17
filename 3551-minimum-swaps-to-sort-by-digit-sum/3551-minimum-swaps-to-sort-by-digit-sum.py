class Solution:
    def minSwaps(self, a: List[int]) -> int:
        b = sorted(a,key=lambda v:(sum(map(int,str(v))),v))
        d,res = dict(zip(a,count())),0
        for v,u in zip(a,b):
            if v!=u: a[d[u]],d[v],res = v,d[u],res+1

        return res