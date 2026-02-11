class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Check if there is extra char for one of them
        if len(word1) != len(word2):
            return False

        # Find uncommon characters
        set1 = set(word1)
        set2 = set(word2)
        # If there is uncommon char
        if set1 ^ set2 != set():
            return False

        #Count number of chars
        ch_count1 = Counter(word1)
        ch_count2 = Counter(word2)

        # Check proportionality of the char counts
        # It means checking if I can attain one from other

        # Populate lists of counts
        list1 = []
        list2 = []
        for count in ch_count1.values():
            list1.append(count)
        for count in ch_count2.values():
            list2.append(count)

        # Sort the lists of counts
        list1.sort()
        list2.sort()

        return list1 == list2
