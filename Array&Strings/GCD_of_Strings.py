class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
        
        # Get the GCD length
        gcd_len = gcd(len(str1), len(str2))
        
        # Return the substring of that length
        # We can take it from either str1 or str2 as they'll be equal
        return str1[:gcd_len]
    
if __name__ == "__main__":

    ob = Solution()

    str1 = input(str("Enter first string: "))
    str2 = input(str("Enter second string: "))

    res = ob.gcdOfStrings(str1, str2)

    print("Greatest Common Divisor of both strings is: ", res)