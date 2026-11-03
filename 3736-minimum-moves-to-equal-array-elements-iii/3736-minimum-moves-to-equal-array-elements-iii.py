class Solution:
    def minMoves(self, nums: List[int]) -> int:
        x=max(nums)
        ctr=0
        for i in nums:
            ctr+=x-i
        return ctr
        