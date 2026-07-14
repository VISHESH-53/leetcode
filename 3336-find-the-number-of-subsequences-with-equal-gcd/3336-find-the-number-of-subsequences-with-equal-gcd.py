class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        @lru_cache(None)
        def solve(idx, g1, g2):
            if idx == n:
                return int(g1 != 0 and g1 == g2)

            x = nums[idx]

            ans = solve(idx + 1, g1, g2)
            ans += solve(idx + 1, gcd(g1, x), g2)
            ans += solve(idx + 1, g1, gcd(g2, x))

            return ans % MOD

        return solve(0, 0, 0)