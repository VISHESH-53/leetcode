class Solution:
    def minMoves(self, nums: list[int]) -> int:
        x=0
        n=min(nums)
        for i in nums:
            x+=i-n
        return x
        