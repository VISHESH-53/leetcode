class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        ctr=0
        for i in range(1000,n+1):
            x=(len(str(i))-1)//3
            ctr+=x
        return ctr

        