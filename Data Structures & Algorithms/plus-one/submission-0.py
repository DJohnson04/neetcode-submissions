class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for num in digits:
            s += str(num)
        print(s)
        s = int(s)
        s += 1
        s = str(s)
        l = []
        for char in s:
            l.append(char)
        return l

                