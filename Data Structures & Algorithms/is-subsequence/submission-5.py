class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = 0
        j = 0

        if t == "":
            return False

        while i < len(t) and j < len(s):
            if s[j] == t[i]:
                i += 1
                j += 1
            else:
                i += 1
        if j == len(s) or j == 0 :
            return True

        return False




            
        

        

        