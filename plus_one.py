class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        for i in range(len(digits)):
            if digits[i] < 9:
                digits[i] += 1
                break
            elif digits[i] == 9:
                digits[i] = 0
                if i == len(digits)-1:
                    digits.append(1)
        digits.reverse()
        return digitss