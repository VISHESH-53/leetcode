class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            ans = 0

            for mask in range(1, 1 << n):
                mul = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        mul = lcm(mul, coins[i])
                        bits += 1

                        if mul > x:
                            break

                if mul <= x:
                    if bits % 2:
                        ans += x // mul
                    else:
                        ans -= x // mul

            return ans

        left = min(coins)
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left

        return prev
