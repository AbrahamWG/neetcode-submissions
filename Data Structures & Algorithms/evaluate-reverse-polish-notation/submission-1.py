class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # value1 value2 sign - > becomes value1 again

        def compute(a, b, sign):
            return signs.get(sign)(int(a), int(b))

        signs = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }

        stack = []

        for i in tokens:
            stack.append(i)
            if i in signs.keys():
                sign, b, a = stack.pop(), stack.pop(), stack.pop()
                stack.append(compute(a, b, sign))

        return int(stack.pop())
        


        