class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        my_dict = {}
        L = 0
        result = 0

        for R in range(len(s)):
            char = s[R]
            if char in my_dict and my_dict[char] >= L:
                L = my_dict[char] + 1

            my_dict[char] = R
            result = max(result, R - L + 1)
            


        return result
            


        