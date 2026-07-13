class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        l = []
        x = len(str(low))

        while x <= len(str(high)):
            n = int("123456789"[:x])
            j = int("1" * x)

            for i in range(10 - x):
                if low <= n <= high:
                    l.append(n)
                n += j

            x += 1

        return l