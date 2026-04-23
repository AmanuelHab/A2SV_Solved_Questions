class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)

        answers = []
        def visit(path):
            if path[-1] == n - 1:
                answers.append(path)
                return
            for nbr in graph[path[-1]]:
                if nbr not in path:
                    visit(path + [nbr])
        visit([0])
        return answers