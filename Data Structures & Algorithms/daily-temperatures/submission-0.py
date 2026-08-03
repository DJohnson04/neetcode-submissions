class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while len(stack) != 0 and temp > stack[-1][1]:
                removed = stack.pop(-1)
                result[removed[0]] = index - removed[0]
            stack.append((index, temp))

        return result

