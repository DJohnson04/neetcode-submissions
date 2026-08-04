class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        curr = n
        while curr not in seen:
            sum = 0
            for char in str(curr):
                sum += int(char)**2
            seen.append(curr)
            print(sum)
            curr = sum
            if curr == 1:
                return True
            
        return False


