class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w=2
        for i in range(2, len(nums)):
            
            if nums[i] != nums[w - 2]:
                nums[w] = nums[i]
                w += 1
                
        return w

        