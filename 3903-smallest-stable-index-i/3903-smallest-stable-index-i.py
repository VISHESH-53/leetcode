class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            ma=max(nums[:i+1])
            mi=min(nums[i:])
            if ma-mi<=k:
                return i
        return -1    

        