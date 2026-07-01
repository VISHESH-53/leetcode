class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:]=nums1[0:m]+nums2[0:n]
        return nums1.sort()
        """
        Do not return anything, modify nums1 in-place instead.
        """
        