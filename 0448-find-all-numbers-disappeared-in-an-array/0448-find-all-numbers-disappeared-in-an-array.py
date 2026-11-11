class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        s = set(nums)
        ans = []
        for i in range(1, len(nums) + 1):
            if i not in s:
                ans.append(i)
        return ans