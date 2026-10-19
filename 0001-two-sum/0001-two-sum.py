class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        d={}
        for i in range(n):
            rem=target-nums[i]
            if rem in d:
                return [d[rem],i]
            d[nums[i]]=i
        