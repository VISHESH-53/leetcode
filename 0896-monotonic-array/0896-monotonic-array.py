class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def inc(nums):
            pred = -float('inf')
            for i in nums:
                if i < pred:
                    return False
                pred = i
            return True

        def dec(nums):
            pred = float('inf')
            for i in nums:
                if i > pred:
                    return False
                pred = i
            return True
        
        return inc(nums) or dec(nums)