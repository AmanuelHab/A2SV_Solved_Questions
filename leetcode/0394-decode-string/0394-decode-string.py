class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            # If there is a word
            if ch == ']':
                char = stack.pop()
                word = ""
                # Collect the word
                while char != '[':
                    word = char + word
                    char = stack.pop()
                
                #Collect k
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                # Input the decoded word
                stack.append(int(num) * word)
            else:
                stack.append(ch)

        return "".join(stack)