class Solution:
    """
    @param: n: The integer
    @return: Roman representation
    """
    def parse(self, digit, index):
        NUMS = {
            1: 'I',
            2: 'II',
            3: 'III',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX'
        }

        ROMAN = {
            'I': ['I', 'X', 'C', 'M'],
            'V': ['V', 'L', 'D', '?'],
            'X': ['X', 'C', 'M', '?']
        }

        num = NUMS[digit]
        return num.replace('X', ROMAN['X'][index]
            ).replace('I', ROMAN['I'][index]).replace('V', ROMAN['V'][index])

    def intToRoman(self, n):
        result = ''
        index = 0
        while n != 0:
            digit = n % 10
            if digit != 0:
                result = self.parse(digit, index) + result
            n /= 10
            index += 1
        return result
