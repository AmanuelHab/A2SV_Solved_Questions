class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        curr_money = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            if bill == 20:
                if curr_money[5] == 0 or (curr_money[10] == 0 and curr_money[5] < 3):
                    return False
                curr_money[5] -= 1
                if curr_money[10]:
                    curr_money[10] -= 1
                else:
                    curr_money[5] -= 2
                curr_money[20] += 1
            elif bill == 10:
                if curr_money[5] == 0:
                    return False
                curr_money[5] -= 1
                curr_money[10] += 1
            else:
                curr_money[5] += 1
                
        return True