import math
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x=str(n)
        s=sum(map(int, str(n)))
        p=math.prod(map(int,str(n)))

        if n%(p+s)==0:
            return True
        else:
            return False

