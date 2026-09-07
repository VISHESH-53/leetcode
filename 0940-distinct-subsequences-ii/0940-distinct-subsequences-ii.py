class Solution:
    def distinctSubseqII(self, s: str) -> int:
        ans={""}
        for i in s:
            n=set()
            for j in ans:
                n.add(j+i)
            ans.update(n)
        ans.remove("")
        return (len(ans) ) % (10**9 + 7)
        