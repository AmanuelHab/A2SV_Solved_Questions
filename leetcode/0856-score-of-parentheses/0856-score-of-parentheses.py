class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for ch in s:
            # If there is a closing parenthesis
            if ch == ')':
                # Collect number if any
                num = 0
                while stack and stack[-1] != '(':
                    num += stack.pop()
                stack.pop() # Remove the opening parenthesis
                if num:
                    stack.append(num * 2)
                else:
                    stack.append(1)
            else:
                stack.append(ch)
        return sum(stack)