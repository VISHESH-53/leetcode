class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        for i in range(k,max(nums)+k+1):
            if i%k==0 and i not in nums:
                return i
        