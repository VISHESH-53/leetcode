class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=""
        l=[]
        for i in str(n):
            if int(i)==0:
                pass
            else:
                l.append(int(i))
                x=x+i
        z=sum(l)
        if x=="":
            return 0
        return int(x)*z



        