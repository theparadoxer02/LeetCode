class Solution:
    def prevSmaller(self, A):
        stack = []
        final_arr = []

        for elem in A:
            # Pop elements from the stack that are greater or equal to the current element
            while stack and stack[-1] >= elem:
                stack.pop()

            # If the stack is empty, no smaller element was found
            if not stack:
                final_arr.append(-1)
            else:
                final_arr.append(stack[-1])

            # Push the current element to the stack
            stack.append(elem)

        return final_arr

s = Solution()

A = [4, 5, 2, 10, 8]

result = s.prevSmaller(A=A)
print(result)

[4, 5, 2, 10, 8]