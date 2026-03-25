class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        strings = set()
        def validP(s):
            stack = []
            for ch in s:
                if ch == ')':
                    if not stack:
                        return False
                    else:
                        stack.pop()
                elif ch == '(':
                    stack.append(ch)
            if stack:
                return False
            return True
        seen = set()
        def generate(s, opening, closing):
            if opening == closing and validP(s):
                strings.add(s)
                return
            if s in seen:
                return
            seen.add(s)
            
            ind = s.find('(')
            while ind != -1:
                new_s = s[:ind] + s[ind + 1:]
                generate(new_s, opening - 1, closing)
                ind = s.find('(', ind + 1)

            ind = s.find(')')
            while ind != -1:
                new_s = s[:ind] + s[ind + 1:]
                generate(new_s, opening, closing - 1)
                ind = s.find(')', ind + 1)

        opening = closing = 0
        for ch in s:
            if ch == '(':
                opening += 1
            elif ch == ')':
                closing += 1
        generate(s, opening, closing)

        max_len = 0
        for st in strings:
            max_len = max(len(st), max_len)

        answer = [st for st in strings if len(st) == max_len]
        if not answer:
            return [""]
        return answer