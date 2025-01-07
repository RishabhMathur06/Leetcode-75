class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'A','E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        #vowels = ('AEIOUaeiou')
        words = list(s)
        l, r = 0, len(s) -1
        while l < r:
            if words[l] in vowels:
                if words[r] in vowels:
                    words[l], words[r] = words[r] , words[l]
                    r -= 1
                    l += 1
                else:
                    r -= 1
            else:
                l += 1
        return ''.join(words)
    
if __name__ == "__main__":
    ob = Solution()

    string = "IceCreAm"

    res = ob.reverseVowels(string)