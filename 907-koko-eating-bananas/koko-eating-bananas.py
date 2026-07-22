class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        while l <= r:
            speed = (l+r) //2
            totalh =0
            for pile in piles:
                totalh += ceil(pile/speed)
            if totalh > h:
                l = speed+1
            else:
                r = speed-1
                
        return l



        