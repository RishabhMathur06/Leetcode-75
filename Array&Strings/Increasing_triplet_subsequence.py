class Solution:
    def increasingTriplet(self, nums) -> bool:
        INF = float("infinity")
        i = INF
        j = INF

        for x in nums:
            if x > j:
                return True
            if x > i:
                j = min(x, j)
            i = min(x, i)
        return False
