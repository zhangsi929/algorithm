from typing import List
class Solution:
    
    def maxLength(sefl, ribbons: List[int], k: int) -> int:
        max_len = sum(ribbons) // k
        l = 1
        r = max_len
        while l + 1 < r:
            mid = (l + r) // 2
            if self.valid(ribbons, mid, k):
                l = mid
            else:
                r = mid
        
        if self.valid(ribbons, r, k):
            return r
        if self.valid(ribbons, l, k):
            return l

        return 0

    def valid(self, ribbons, length, k):
        total = 0
        for n in ribbons:
            total += n // length
            if total >= k:
                return True
        return False
