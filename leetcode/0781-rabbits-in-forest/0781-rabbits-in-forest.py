class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        n = len(answers)

        counter = Counter(answers)
        total = 0
        print(counter)
        for ans, count in counter.items():
            there_are = ans + 1
            total += math.ceil(count / there_are) * there_are
        return total