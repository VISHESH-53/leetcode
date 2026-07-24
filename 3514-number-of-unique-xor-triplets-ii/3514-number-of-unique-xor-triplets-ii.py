class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        distinct_nums = set(nums)
        S = {0}
        for _ in range(3):
            new_set = set()
            for x in S:
                for a in distinct_nums:
                    new_set.add(x ^ a) 
            S = new_set 
        return len(S)
