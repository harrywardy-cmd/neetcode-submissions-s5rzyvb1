class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = 0
        result = 0

        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                x = i
                break
        for j in range(x, -1,-1):
            if s[j] != " ":
                result += 1
            else:
                break
                
        return result
