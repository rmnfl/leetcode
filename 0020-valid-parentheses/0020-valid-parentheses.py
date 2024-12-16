class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            else:
                if not stack or stack.pop() != mapping[char]:
                    return False
        if stack:
            return False
        return True