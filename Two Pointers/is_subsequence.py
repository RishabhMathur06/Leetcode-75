class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        n = len(t)
        m = len(s)

        count = 0

        if(s==""):
            return True
            
        while(i < n):
            j = j%m
            if(t[i]==s[j]):
                count += 1
                i += 1
                j += 1

            else:
                i += 1

        if(count == len(s)):
            return True
        else:
            return False
        
if __name__ == "__main__":
    ob = Solution()

    s = "abc"
    t = "ahbgdc"

    print(ob.isSubsequence(s, t))