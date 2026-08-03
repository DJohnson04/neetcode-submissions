class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalidrome(self, l_in, r_in):
            l, r = l_in, r_in 
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return isPalidrome(self, l + 1, r) or isPalidrome(self, l, r-1)
            else: 
                l += 1  
                r -= 1
        return True
