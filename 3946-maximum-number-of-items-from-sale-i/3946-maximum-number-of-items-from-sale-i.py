class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        f = [0] * (budget + 1)
        mn = min(price for _, price in items)

        for i, (factor, price) in enumerate(items):
            cnt = sum(
                1 for j, (other_factor, _) in enumerate(items)
                if i != j and other_factor % factor == 0
            )

            for j in range(budget, price - 1, -1):
                f[j] = max(f[j], f[j - price] + cnt + 1)

        return max(
            f[j] + (budget - j) // mn
            for j in range(budget + 1)
        )