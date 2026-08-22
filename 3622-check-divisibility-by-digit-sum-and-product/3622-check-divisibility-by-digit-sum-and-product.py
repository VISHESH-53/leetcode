class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x=str(n)
        s=0
        p=1
        for i in x:
            s+=int(i)
            p*=int(i)
        if n%(p+s)==0:
            return True
        else:
            return False

