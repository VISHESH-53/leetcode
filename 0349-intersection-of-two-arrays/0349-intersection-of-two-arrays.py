class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=set(nums1)
        l=[]
        for i in x:
            if i in nums2:
                l.append(i)
        return l
        
        