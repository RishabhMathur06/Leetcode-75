class Solution:
    def canPlaceFlowers(flowerbed, n):
        # Base case
        if(n==0):
            return True
        embedded = [0] + flowerbed + [0]
        count = 0

        for i in range(1, len(embedded)-1):
            if(embedded[i]==0 and embedded[i-1]==0 and embedded[i+1]==0):
                embedded[i] = 1
                count += 1

                if(count >= n):
                    return True

        return False

if __name__ == "__main__":
    ob = Solution()

    flowerbed = [1, 0, 0, 0, 1]
    new_flowers = 1

    output = ob.canPlaceFlowers(flowerbed, new_flowers)

    print(output)