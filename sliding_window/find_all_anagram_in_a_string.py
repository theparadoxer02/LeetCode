from typing import List
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N = len(s)
        k = len(p)
        final_array = []

        if N < k:
            return final_array

        char_dict = {}
        for char in p:
            char_dict[char] = 1 + char_dict.get(char, 0)

        count = len(char_dict)

        right = 0
        left = 0
        while right < N:
            if s[right] in char_dict:
                char_dict[s[right]] -= 1

                if char_dict[s[right]] == 0:
                    count -= 1

            right += 1
    
            if right - left >= k:
                if count == 0:
                    final_array.append(left)
                
                if s[left] in char_dict:
                    char_dict[s[left]] += 1
                
                    if char_dict[s[left]] == 1:
                        count += 1
                left += 1
            
        return final_array
 
                


S = Solution()
s = "cbaebabacd"
p = "abc"

s = "abab"
p = "ab"

s = "baa"
p = "aa"

result = S.findAnagrams(s=s, p=p)
print(result)


s = "cbaebabacd"
p = "abc"

counter =  3

dict = {
    'a': 1,
    'b': 1,
    'c': 1
}

index = 0
s = "cbaebabacd"

left = 0, right = 2
