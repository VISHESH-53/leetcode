class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if len(nums)<3:
            return len(nums)
        else:
            return 1<<len(nums).bit_length()

        