<<<<<<< HEAD
class MinStack:

    def __init__(self):
        self.stack = [(-1, float('inf'))]

    def push(self, x):
        self.stack.append([x, min(x, self.stack[-1][1])])

    def pop(self):
        if len(self.stack) > 1: 
            self.stack.pop()

    def top(self):
        if len(self.stack) == 1: 
            return None
        return self.stack[-1][0]

    def getMin(self):
=======
class MinStack:

    def __init__(self):
        self.stack = [(-1, float('inf'))]

    def push(self, x):
        self.stack.append([x, min(x, self.stack[-1][1])])

    def pop(self):
        if len(self.stack) > 1: 
            self.stack.pop()

    def top(self):
        if len(self.stack) == 1: 
            return None
        return self.stack[-1][0]

    def getMin(self):
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
        return self.stack[-1][1]