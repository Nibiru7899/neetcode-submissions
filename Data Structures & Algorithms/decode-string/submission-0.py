class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                k = ""
                while stack[-1] != "[":
                    k = stack.pop()+k
                stack.pop()

                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop()+num
                stack.append(int(num)*k)
        return "".join(stack)
