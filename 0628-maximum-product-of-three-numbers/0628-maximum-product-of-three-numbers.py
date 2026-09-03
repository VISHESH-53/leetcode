class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max_three = heapq.nlargest(3, nums)

        min_two = heapq.nsmallest(2, nums)
        
        return max(
            max_three[0] * max_three[1] * max_three[2],
            min_two[0] * min_two[1] * max_three[0]
        )

        