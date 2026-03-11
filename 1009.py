class Solution:
    def bitwiseComplement(self, n: int) -> int:
        x=format(n,'b')
        comp=""
        for i in x:
            if i=="0":
                comp=comp+"1"
            else:
                comp=comp+"0"
        return int(comp,2)
