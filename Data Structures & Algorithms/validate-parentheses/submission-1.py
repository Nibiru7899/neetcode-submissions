class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            "]":"[",
            ")":"(",
            "}":"{"
        }
        stack = []

        for n in s:
            if n in valid.values():
                stack.append(n)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top!=valid[n]:
                    return False
        return len(stack)==0