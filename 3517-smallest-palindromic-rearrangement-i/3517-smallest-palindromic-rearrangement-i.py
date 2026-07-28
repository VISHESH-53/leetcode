class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        half = sorted(s[:n // 2])

        if n % 2:
            return "".join(half) + s[n // 2] + "".join(reversed(half))
        else:
            return "".join(half) + "".join(reversed(half))