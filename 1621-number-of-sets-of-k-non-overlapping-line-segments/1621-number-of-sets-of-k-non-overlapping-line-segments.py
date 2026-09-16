class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        def factorial(x):
            res=1
            for i in range(2,x+1):
                res*=i
            return res
        a=n+k-1
        b=2*k
        c=factorial(a)
        d=factorial(b)
        e=factorial(a-b)
        f=d*e

        return int((c//f)%(10**9 +7))
        