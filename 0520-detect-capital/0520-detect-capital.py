class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        ctr=0
        for i in word:
            if i.isupper():
                ctr+=1
        if ctr==len(word) or ctr== 0:
            return True
        if ctr==1 and word[0].isupper():
            return True
        else:
            return False
        