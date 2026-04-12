class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            minSpeed = 0
            for i in piles:
                minSpeed += math.ceil(float(i) / mid)
            if minSpeed <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res