class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        p = 0
        f = flowerbed
        while i < len(f):
            if i == 0:
                left = True
            elif f[i-1] == 0:
                left = True
            else:
                left = False
            
            current = (f[i] == 0)

            if i == len(f)-1:
                right = True
            elif f[i+1] == 0:
                right = True
            else:
                right = False
            
            if left and current and right:
                f[i] = 1
                p += 1

            if p >= n:
                return True

            i+= 1
        return False if n > 0 else True
        