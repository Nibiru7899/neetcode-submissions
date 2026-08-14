class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for n in s:
            if n != "]":
                stack.append(n)
            else:
                k = ""
                while stack[-1]!="[":
                    k = stack.pop() + k
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop()+num
                stack.append(int(num)*k)
        return "".join(stack)