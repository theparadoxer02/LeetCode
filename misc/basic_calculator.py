import re


class Solution:
    def calculate(self, s: str) -> int:
        exprs = [char for char in s if char != " "]
        exprs = "".join(exprs)
        custom_splits = re.findall(r'\d+|[+\-*/]', exprs)
        stack = []
        operations = ["/", "*", "+", "-"]

        for index in range(4):
            for elem in custom_splits:
                if not stack:
                    stack.append(elem)
                    continue

                if stack[-1] in operations:
                    if index == 0 and stack[-1] == "/":
                        _ = stack.pop()
                        elem1 = stack.pop()
                        new_val = int(elem1) // int(elem)

                    elif index == 1 and stack[-1] == "*":
                        _ = stack.pop()
                        elem1 = stack.pop()
                        new_val = int(elem1) * int(elem)

                    elif index == 2 and stack[-1] == "+":
                        _ = stack.pop()
                        elem1 = stack.pop()
                        new_val = int(elem1) + int(elem)

                    elif index == 3 and stack[-1] == "-":
                        _ = stack.pop()
                        elem1 = stack.pop()
                        new_val = int(elem1) - int(elem)
                    else:
                        new_val = elem

                    stack.append(new_val)

                else:
                    stack.append(elem)
            
            custom_splits = stack

        return stack


s = Solution()

input_str = "3+2*2"
result = s.calculate(input_str)
print(result)
