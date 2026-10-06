class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ctr1=0
        ctr2=0
        for i in s:
            if i=="(":
                ctr1+=1
            else:
                if ctr1>0:
                    ctr1-=1
                else:
                    ctr2+=1
        return ctr1+ctr2
        