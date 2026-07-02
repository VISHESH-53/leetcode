class Solution:
    def isPalindrome(self, s: str) -> bool:
        c="".join(filter(str.isalnum,s)).lower()
        n=len(c)
        for i in range(0,n//2):
            if c[i]!=c[n-i-1]:
                return False
        return True