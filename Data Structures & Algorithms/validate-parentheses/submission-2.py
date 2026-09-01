class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            ']' : '[',
            ')' : '(',
            '}' : '{'
        }
        stack = []
        for ch in s:
            if ch not in ']})':
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != valid[ch]:
                    return False
        return len(stack) == 0