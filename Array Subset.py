#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        if len(b) > len(a):
            return False
        a_count = dict()
        b_count = dict()
        for num in a:
            a_count[num] = a_count.get(num, 0) + 1
        for num in b:
            b_count[num] = b_count.get(num, 0) + 1
        for key, value in b_count.items():
            if key not in a_count:
                return False
            if value > a_count[key]:
                return False
        return True
