class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi= max(candies)
        o = []
        for i in candies:
            if i + extraCandies >= maxi:
                o.append(True)
            else:
                o.append(False)
            
        return o