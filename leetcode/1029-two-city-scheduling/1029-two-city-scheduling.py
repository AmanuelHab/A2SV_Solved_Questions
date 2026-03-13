class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costs.sort(key=lambda x: (x[0] - x[1]))
        print(costs)

        cost = 0
        for i in range(n // 2):
            cost += costs[i][0] + costs[n - i - 1][1]
        return cost