class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        count1 = Counter(s1)
        count2 = Counter(s2)

        x_c = count1['x'] + count2['x']
        y_c = count1['y'] + count2['y']

        if x_c % 2 or y_c % 2:
            return -1
        x_y = 0
        y_x = 0
        for i in range(len(s1)):
            if s1[i] == 'x' and s2[i] == 'y':
                x_y += 1
            elif s1[i] == 'y' and s2[i] == 'x':
                y_x += 1
        
        # Apply formula
        return x_y // 2 + y_x // 2 + (x_y % 2  + y_x %2)
       
