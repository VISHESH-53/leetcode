class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if nums == sorted(nums) or nums== sorted(nums,reverse=True):
            return True
        return False 

        