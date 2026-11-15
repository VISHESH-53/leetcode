class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9+7
        prefix_sum = 0
        oddCount = 0

        for a in arr:
            prefix_sum+=a
            oddCount+=prefix_sum%2

        oddCount+=(len(arr)-oddCount)*oddCount

        return  oddCount%MOD