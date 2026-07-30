class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        res=0
        p=1
        while n>=8:
            res+=(8*p)
            p+=1
            n-=8
        res+=(n*p)
        return res
        