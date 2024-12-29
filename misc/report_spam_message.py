from typing import List


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned_dict = {}
        for banned in bannedWords:
            banned_dict[banned] = 0

        for word in message:
            if word in banned_dict:
                banned_dict[word] = banned_dict[word] + 1

                if banned_dict[word] >= 2:
                    return True
        
        return False

s = Solution()
message = ["hello","world","leetcode"]
bannedWords = ["world","hello"]
result = s.reportSpam(message=message, bannedWords=bannedWords)
