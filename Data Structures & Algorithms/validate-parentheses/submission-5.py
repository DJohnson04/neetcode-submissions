class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        valid = {'}': '{', ')': '(', ']': '['}
        for char in s:
            if char == '[' or char == '(' or char == '{':
                arr.append(char)
            else:
                if len(arr) == 0: return False
                if valid[char] != arr.pop(-1):
                    return False
        if len(arr) != 0:
            return False 
        
        return True
                                                                                