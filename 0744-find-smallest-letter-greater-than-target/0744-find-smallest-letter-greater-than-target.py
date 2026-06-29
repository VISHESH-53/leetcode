class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l1=[]
        res=""

        for i in letters:
            if ord(i)>ord(target):
                l1.append(ord(i))
        if len(l1)==0:
            return letters[0]
        return chr(min(l1))
        
        