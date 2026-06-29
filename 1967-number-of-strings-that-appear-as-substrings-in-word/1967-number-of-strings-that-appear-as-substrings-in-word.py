class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ctr=0
        for i in patterns:
            if i in word:
                ctr+=1
        return ctr
        