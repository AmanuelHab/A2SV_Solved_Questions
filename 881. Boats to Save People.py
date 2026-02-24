class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()

        boats = 0
        i, j = 0, n - 1
        while i < j:
        # Find possible pair transportation
            if people[i] + people[j] <= limit:
                boats += 1
                i += 1
                j -= 1
        # Else transport the heaviest
            else:
                boats += 1
                j -= 1
                
        # If there is remaining person
        if i == j:
            boats += 1

        return boats
