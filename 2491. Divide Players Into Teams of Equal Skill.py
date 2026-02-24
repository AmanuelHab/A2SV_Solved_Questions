class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()

        total = sum(skill)
        pair_sum = total / n * 2

        chemistry = 0
        for i in range(n // 2):
            if skill[i] + skill[n - i - 1] != pair_sum:
                return -1
            chemistry += skill[i] * skill[n - i - 1]
        return chemistry
