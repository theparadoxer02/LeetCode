
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        n = len(s)
        max_length = 0

        charset = set()

        for right in range(n):
            if s[right] not in charset:
                max_length = max(max_length, right-left + 1)
                charset.add(s[right])

            else:
                while s[right] in charset:
                    charset.remove(s[left])
                    left += 1
                charset.add(s[right])

        return max_length
        
