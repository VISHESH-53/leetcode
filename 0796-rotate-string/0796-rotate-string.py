class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        f=s+s
        if goal in f and len(s)==len(goal):
            return True
        return False
        