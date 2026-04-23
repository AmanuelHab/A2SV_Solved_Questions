class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        # DAG
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if i != j:
                    xi, yi, ri = bombs[i]
                    xj, yj, rj = bombs[j]
                    dist = math.sqrt(abs(xi-xj) ** 2 + abs(yi-yj)** 2)
                    if dist <= ri:
                        graph[i].append(j)
                    if dist <= rj:
                        graph[j].append(i)
       
        def detonate(bomb):
            detonated.add(bomb)
            for nbr in graph[bomb]:
                if nbr not in detonated:
                    detonate(nbr)
        detonated = set()
        max_det = 0
        for i in range(n):
            detonate(i)
            max_det = max(max_det, len(detonated))
            detonated.clear()
        return max_det