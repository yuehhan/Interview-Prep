# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

def letterCombinations(self, digits: str) -> List[str]:
    if not digits: return []
    numbers = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
    }
    ans = []
    current = ""
    index = 0


    def generate(current, digits, index):
        if len(current) == len(digits):
            ans.append(current)
            return
        for i in numbers[digits[index]]:
            generate(current+i, digits, index+1)
            
    generate(current, digits, index)
    return ans