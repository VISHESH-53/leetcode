class Solution:
    def rob(self, nums: List[int]) -> int:
        ctr1, ctr2 = 0, 0
        for i in nums:
            cur = max(ctr1, ctr2 + i )
            ctr1, ctr2 = cur, ctr1
        return cur

        