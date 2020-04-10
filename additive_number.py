# Additive number is a string whose digits can form additive sequence.

# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

# Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

class Solution:
    
    def isAdditiveNumber(self, num: str) -> bool:
        for i in range(1, len(num)):
            for j in range(i+1, len(num)):
                first = num[:i]
                second = num[i:j]
                rest = num[j:]
                
                if first[0] == '0' and first!= '0'or second[0] == '0' and second != '0' or rest[0] == '0' and rest != '0':
                    continue
                
                while len(rest) > 0:
                    third = str(int(first) + int(second))
                    if rest[:len(third)] != third:
                        break
                    else:
                        first = second
                        second = third
                        rest = rest[len(third):]
                if len(rest) == 0:
                    return True
        
        return False