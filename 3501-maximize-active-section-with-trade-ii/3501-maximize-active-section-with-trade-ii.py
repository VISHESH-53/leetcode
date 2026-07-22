class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        ones = s.count('1')
        zs, ze = zip(*((mo.start(), mo.end() - 1) for mo in re.finditer('0+', s))) if '0' in s else ((), ())
        nblocks = len(zs)
        V = list(map(sum, pairwise(b - a + 1 for a, b in zip(zs, ze))))
        nv = len(V)
        sparse = [V]
        half = 1
        while half * 2 <= nv:
            prev = sparse[-1]
            sparse.append(list(map(max, prev, prev[half:])))
            half *= 2
        def rmq(lo, hi):
            t = (hi - lo + 1).bit_length() - 1
            return max(sparse[t][lo], sparse[t][hi - (1 << t) + 1])
        def clip(j, l, r):
            return V[j] - max(0, l - zs[j]) - max(0, ze[j + 1] - r)
        def gain(l, r):
            if nblocks < 2:
                return 0
            ja = bisect_left(ze, l)
            jb = bisect_right(zs, r) - 2
            if ja > jb:
                return 0
            return max(clip(ja, l, r),clip(jb, l, r),rmq(ja + 1, jb - 1) if jb - ja >= 2 else 0)
        return [ones + gain(l, r) for l, r in queries]