class Solution:
    def intToRoman(self, num: int) -> str:
        thousands = num // 1000
        num %= 1000
        hundreds = num // 100
        num %= 100
        tens = num // 10
        ones = num % 10

        roman = ""
        if thousands:
            roman += "M" * thousands
        if hundreds:
            if hundreds == 4:
                roman += "CD"
            elif hundreds == 9:
                roman += "CM"
            elif hundreds < 4:
                roman += "C" * hundreds
            else:
                roman += "D" + "C" * (hundreds - 5)
        if tens:
            if tens == 4:
                roman += "XL"
            elif tens == 9:
                roman += "XC"
            elif tens < 4:
                roman += "X" * tens
            else:
                roman += "L" + "X" * (tens - 5)
        if ones:
            if ones == 4:
                roman += "IV"
            elif ones == 9:
                roman += "IX"
            elif ones < 4:
                roman += "I" * ones
            else:
                roman += "V" + "I" * (ones - 5)
        return roman
