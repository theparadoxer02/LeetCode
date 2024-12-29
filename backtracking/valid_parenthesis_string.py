class Solution:
    def checkValidString(self, s: str) -> bool:
        pass
        
    def is_valid_string(self, string):
        stack = []
        for char in string:
            if char == ')' and not stack:
                return False
            
            elif char == ')' and stack[-1] != '(':
                return False
            
            elif char == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
        
        return True
        
        

s = Solution()


string = '(()))'
result = s.is_valid_string(string)
print(result)