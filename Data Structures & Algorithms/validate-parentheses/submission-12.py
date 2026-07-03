class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for  parentheses in s:
            if parentheses in closeToOpen:
                if stack and stack[-1] == closeToOpen[parentheses]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(parentheses)
        return not bool(stack)

