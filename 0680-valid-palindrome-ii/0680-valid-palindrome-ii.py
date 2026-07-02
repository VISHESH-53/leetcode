class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:

                skip_left = s[left+1 : right+1]
                skip_right = s[left : right]

                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
            
            left += 1
            right -= 1
            
        return True
