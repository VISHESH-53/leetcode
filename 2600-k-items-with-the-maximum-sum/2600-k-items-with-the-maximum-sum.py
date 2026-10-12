class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes+numZeros<k:
            return numOnes-(k-(numOnes+numZeros))
        else:
            return min(numOnes,k)
        