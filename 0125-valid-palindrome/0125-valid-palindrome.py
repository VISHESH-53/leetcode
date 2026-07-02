class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = "".join(filter(str.isalnum, s)).lower()
        
        return cleaned == cleaned[::-1]
