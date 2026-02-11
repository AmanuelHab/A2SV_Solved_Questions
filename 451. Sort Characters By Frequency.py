class Solution:
    def frequencySort(self, s: str) -> str:
        # Count frequency
        ch_count = Counter(s)

        # Return the string after sorting decreasingly by their frequency
        return "".join(sorted(s, key=lambda x: (-ch_count[x], x)))
