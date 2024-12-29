from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        total_valid_substrings = 0
        
        for left in range(n):
            vowel_count = defaultdict(int)
            consonant_count = 0
            unique_vowels = 0  # Number of unique vowels in the current substring

            for right in range(left, n):
                c = word[right]
                if c in vowels:
                    if vowel_count[c] == 0:
                        unique_vowels += 1
                    vowel_count[c] += 1
                else:
                    consonant_count += 1

                # If consonant count exceeds k, no need to consider longer substrings starting at `left`
                if consonant_count > k:
                    break

                # If all vowels are present and consonant count equals k
                if unique_vowels == 5 and consonant_count == k:
                    total_valid_substrings += 1

        return total_valid_substrings

# Example usage:
solution = Solution()
print(solution.countOfSubstrings("iqeaouqi", 1))  # Output: 3

