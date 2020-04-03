def isHappy(self, n: int) -> bool:
    string = str(n)
    memory = set()

    while string != '0':
        result = 0
        for i in string:
            result+= int(i)**2
        if result == 1:
            return True
        if result in memory:
            return False
        else:
            string = str(result)
            memory.add(result)

    return False