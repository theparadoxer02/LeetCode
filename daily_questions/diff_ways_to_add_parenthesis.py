from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        def evaluate_exp(expression):
            # Base case: if the expression is a number, return it as a single-element list
            if expression.isdigit():
                return [int(expression)]
            
            res = []
            for i in range(len(expression)):
                if expression[i] in '+-*':
                    # Divide the expression into left and right parts
                    left_exp = evaluate_exp(expression[:i])
                    right_exp = evaluate_exp(expression[i+1:])
                    
                    # Compute all combinations of results from left and right parts
                    for l in left_exp:
                        for r in right_exp:
                            if expression[i] == '+':
                                res.append(l + r)
                            elif expression[i] == '-':
                                res.append(l - r)
                            elif expression[i] == '*':
                                res.append(l * r)


            return res

        return evaluate_exp(expression)


s = Solution()
expression = "2*3-4*5"
result = s.diffWaysToCompute(expression=expression)
print(result)
