import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumodd=n*n
        sumeven=n*(n+1)
        return math.gcd(sumodd,sumeven)
        