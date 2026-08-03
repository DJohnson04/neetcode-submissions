class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:

                if operation == '+':
                    stack.append(stack[len(stack) - 1] + stack[len(stack) - 2])
                elif operation == 'D':
                    stack.append(2 * stack[len(stack) - 1])
                elif operation == 'C':
                    stack.pop(-1)
                else:
                    stack.append(int(operation))
        sum = 0
        for i in stack:
            sum += i
        return sum