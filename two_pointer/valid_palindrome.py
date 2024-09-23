class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        final_str = []
        counter = -1
        if not s:
            return False

        for char in s:
            char_ascii = ord(char)
            if 65 <= char_ascii <= 90:
                final_str.append(char.lower())
                counter += 1

            elif 97 <= char_ascii <= 122:
                final_str.append(char)
                counter += 1

        left = 0
        right = counter

        while left < right:
            if final_str[left] != final_str[right]:
                return False
            else:
                left += 1
                right -= 1

        return True


s = "A man, a plan, a canal: Panamam"
s = "0P"
a = Solution()
result = a.isPalindrome(s)
print(result)
