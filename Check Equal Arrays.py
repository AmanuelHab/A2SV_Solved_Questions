class Solution:
    def checkEqual(self, a, b) -> bool:
        a_count = dict()
        b_count = dict()
        
        for num in a:
            if num in a_count:
                a_count[num] += 1
            else:
                a_count[num] = 1
        for num in b:
            if num in b_count:
                b_count[num] += 1
            else:
                b_count[num] = 1
        for key, value in a_count.items():
            if key not in b_count:
                return False
            if value != b_count[key]:
                return False
        return True
