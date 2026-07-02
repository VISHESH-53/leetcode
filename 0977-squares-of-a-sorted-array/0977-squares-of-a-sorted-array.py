class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            l.append(i*i)
        l.sort()
        return l
            