class Solution:    
    def findUnion(self, a, b):
        union = set()
        for num in a:
                union.add(num)
                
        for num in b:
                union.add(num)
        return union 
