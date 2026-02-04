class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        answer = []
        new_line = ''
        found_mc = False
        for line in source:
            i = 0
            n = len(line)
            while i < n:
                couple = line[i: i+2]
                if couple == '//' and not found_mc:
                    if new_line:
                        answer.append(new_line)
                        new_line = ''
                    break
                elif couple == '/*' and not found_mc:
                    found_mc = True
                    i += 2
                elif couple == '*/' and found_mc:
                    found_mc = False
                    i += 2
                else:
                    if not found_mc:
                        new_line += line[i]
                    i += 1
            if new_line and not found_mc:
                answer.append(new_line)
                new_line = ''
        return answer
