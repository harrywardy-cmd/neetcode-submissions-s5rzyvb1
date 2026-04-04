class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]

        for x in s:
            if x == "{" or x == "(" or x == "[":
                stack.append(x)
            elif bool(stack):
                if x =="]" and stack[-1] == "[" or x =="}" and stack[-1] == "{" or x ==")" and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            else:
                return False    
            

        return not bool(stack)
        