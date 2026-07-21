class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        zeros = map(len, filter(None, s.split("1")))


        maxzeros = max(map(sum, pairwise(zeros)), default=0)

        return s.count("1") + maxzeros

        