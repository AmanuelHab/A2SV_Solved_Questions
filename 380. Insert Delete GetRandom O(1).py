class RandomizedSet:

    def __init__(self):
        self.value_ind = dict()
        self.lst = []
        self.n = 0
        

    def insert(self, val: int) -> bool:
        if val in self.value_ind:
            return False
        else:
            self.value_ind[val] = self.n
            self.lst.append(val)
            self.n += 1
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.value_ind:
            index = self.value_ind[val]
            self.lst[index] = self.lst[-1]
            self.value_ind[self.lst[index]] = index
            self.lst.pop()
            self.value_ind.pop(val)
            self.n -= 1
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.lst)
