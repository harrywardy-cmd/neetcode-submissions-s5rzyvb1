class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        R = 0
        result = 0

        for x in range(len(s)-1,-1,-1):
            if s[x] != " ":
                R = x 
                break
        for y in range(R, -1,-1):
            if s[y] != " ":
                result += 1
            else:
                break


        return result
