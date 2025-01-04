class Solution:
    def kidsWithCandies(self, candies, extra_candies):
        maxm = 0

        n = len(candies)

        for i in range(n):
            maxm = max(candies[i], maxm)

        result = []

        for i in range(n):
            if(candies[i]+extra_candies >= maxm):
                result.append(True)
            else:
                result.append(False)

        return result
    
if __name__ == "__main__":
    ob = Solution()

    candies_with_kid = [2, 3, 5, 1, 3]

    extra_candies = 3

    result = ob.kidsWithCandies(candies_with_kid, extra_candies)

    print(result)