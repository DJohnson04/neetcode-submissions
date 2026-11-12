class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for index,curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                previous_indx = stack.pop()
                result[previous_indx] = index - previous_indx
            stack.append(index)
                
        return result


