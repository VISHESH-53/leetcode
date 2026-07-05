import statistics as s
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return s.mode(nums)
        