from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        seen = set(nums)

        answer = total

        while answer in seen:
            answer += 1

        return answer


        