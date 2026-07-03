class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        my_dict = {}
        L = 0
        result = 0

        for R in range(len(s)): 
            if s[R] in my_dict and my_dict[s[R]] >= L:
                L = my_dict[s[R]] + 1

            my_dict[s[R]] = R
            result = max(result, R - L + 1)
            


        return result
            


        