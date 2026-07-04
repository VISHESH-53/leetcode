class Solution:
    def removeStars(self, s: str) -> str:
        l=[]
        res=""
        for i in s:
            if i=="*":
                l.pop()
            else:
                l.append(i)
        
        for i in l:
            res=res+i
        return res

        