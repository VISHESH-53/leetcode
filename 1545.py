class Solution(object):
    def findKthBit(self, n, k):
        if n == 1:
            return '0'
        
        length = (1 << n) - 1  
        mid = length // 2 + 1
        
        if k == mid:
            return '1'
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            mirror_pos = length - k + 1
            bit = self.findKthBit(n - 1, mirror_pos)
            return '0' if bit == '1' else '1'
