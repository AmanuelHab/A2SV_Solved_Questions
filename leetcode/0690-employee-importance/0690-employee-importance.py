"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        id_imp = dict()
        for emp in employees:
            i, imp, subs = emp.id, emp.importance, emp.subordinates
            id_imp[i] = imp
            for sub in subs:
                graph[i].append(sub)
        imp = 0
        visited = set()
        def recurse(i):
            nonlocal imp
            visited.add(i)
            imp += id_imp[i]

            for neighbour in graph[i]:
                if neighbour not in visited:
                    recurse(neighbour)
        recurse(id)
        return imp
        