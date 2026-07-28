class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate = math.inf
        biggestPile = max(piles)

        searchSpace = range(1, biggestPile + 1)
        l = 0
        r = len(searchSpace) - 1

        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / searchSpace[mid])
            if hours <= h:
                rate = min(rate, searchSpace[mid])
                r = mid - 1
            else:
                l = mid + 1
            
        return rate 

        