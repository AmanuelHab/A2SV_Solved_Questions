class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if sum(changed) % 3 or len(changed) % 2:
            return []

        answer = []
        changed.sort()

        while changed:
            double_val = {num * 2 for num in changed}
            not_doubles = set()
            for num in changed:
                if num not in double_val:# and num /2 not in double_val:
                    not_doubles.add(num)
            if not not_doubles:
                allZ = True
                for n in changed:
                    if n != 0:
                        allZ = False
                        break
                if allZ:
                    answer.extend([0] * (len(changed) // 2))
                    break
                else:
                    return []

            answer.extend(list(not_doubles))
            #Store ones and doubles
            ones = set(not_doubles)
            doubles = set()
            for one in ones:
                doubles.add(one * 2)
                
            new_changed = []
            for num in changed:
                if num in ones and num  in doubles:
                    new_changed.append(num)
                    ones.remove(num)
                elif num in doubles:
                    doubles.remove(num)
                elif num in ones:
                    ones.remove(num)
                else:
                    new_changed.append(num)
            # If there is a double that should has/have been removed
            if doubles != set():
                return []
            changed = new_changed

        return answer
