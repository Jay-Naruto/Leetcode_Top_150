class Solution:
    @staticmethod
    def intToRoman(num: int) -> str:
        romanMap = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
            10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
            100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
            1000: 'M'
        }

        digitMap = {
            3: 1000,
            2: 100,
            1: 10,
            0: 1
        }

        ans = ''
        digits = len(str(num))
        j = 1

        for digit in str(num):
            digit = int(digit)
            placeValue = digitMap[digits - j]

            if digit != 0:
                if digit == 4 or digit == 9:
                    ans += romanMap[digit * placeValue] 
                elif digit >= 5:
                    ans += romanMap[5 * placeValue] 
                    ans += romanMap[placeValue] * (digit - 5) 
                else:
                    ans += romanMap[placeValue] * digit

            j += 1

        return ans
