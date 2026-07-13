class Solution:
    def reverse(self, x: int) -> int:
        y=str(x)
        if y[0]=="-":
            y=str(abs(x))
            z=y[::-1]
            r=int(z)*-1
            return r if r>=-2**31 else 0
        z=y[::-1]
        r=int(z)
        return r if r<=2**31 else 0
        