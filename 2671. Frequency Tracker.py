class FrequencyTracker:

    def __init__(self):
        self.array = []
        self.num_freq = defaultdict(int)
        self.freq_total = defaultdict(int)

    def add(self, number: int) -> None:
        self.array.append(number)
        freq = self.num_freq[number]
        self.num_freq[number] += 1
        self.freq_total[freq] -= 1
        self.freq_total[freq + 1] += 1


    def deleteOne(self, number: int) -> None:
        if self.num_freq[number]:
            self.array.remove(number)
            freq = self.num_freq[number]
            self.num_freq[number] -= 1
            self.freq_total[freq] -= 1
            self.freq_total[freq - 1] += 1
        

    def hasFrequency(self, frequency: int) -> bool:
        return True if self.freq_total[frequency] > 0 else False
