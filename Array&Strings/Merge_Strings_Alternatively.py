class Solution:
    def mergeStrings(self, word1, word2):
        print(f'\nReceived words: "{word1}" & "{word2}".')
        print('\nMerging...')
        
        i, j = 0, 0

        res = ""
        n = len(word1)
        m = len(word2)

        while(i<n and j<m):
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1

        while(i<n):
            res += word1[i]
            i += 1

        while(j<m):
            res += word2[j]
            j += 1

        return res

if __name__ == '__main__':
    word1 = input("\nEnter first word: ")
    word2 = input("Enter second word: ")

    ob = Solution()

    ans = ob.mergeStrings(word1, word2)

    print(f'\nMerge Successful!')
    print(f"New String: {ans}")