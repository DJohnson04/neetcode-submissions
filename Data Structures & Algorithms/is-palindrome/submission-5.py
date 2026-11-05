class Solution:
    def is_alphanumeric(self, char):
        if "a" <= char <= "z" or "A" <= char <= "Z" or "0" <= char <= "9":
            return True
        return False
    def isPalindrome(self, s: str) -> bool:
        l_p, r_p = 0, len(s) - 1
        while l_p < r_p:
            while l_p < r_p and not self.is_alphanumeric(s[l_p]):
                l_p+=1 
            while l_p < r_p and not self.is_alphanumeric(s[r_p]):
                r_p -= 1
            if s[l_p].lower() != s[r_p].lower():
                return False
            l_p += 1
            r_p -= 1
        return True