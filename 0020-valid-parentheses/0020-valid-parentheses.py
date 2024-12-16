class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if not stack:
                    return False
                match char:
                    case ')':
                        if stack[-1] != '(':
                            return False
                        stack.pop()
                    case '}':
                        if stack[-1] != '{':
                            return False
                        stack.pop()
                    case ']':
                        if stack[-1] != '[':
                            return False
                        stack.pop()
            
        if stack:
            return False
        return True