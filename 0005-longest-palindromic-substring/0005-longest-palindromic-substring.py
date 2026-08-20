class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=set()
        def expand(l:int,r:int):
            while l>=0 and r<len(s) and s[l]==s[r]:
                res.add(s[l:r+1])
                l-=1
                r+=1
        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)
        a=list(res)
        if not a:
            return ""
        x=0
        ans=""
        for j in a:
            if len(j)>x:
                x=len(j)
                ans=j
        return ans


        