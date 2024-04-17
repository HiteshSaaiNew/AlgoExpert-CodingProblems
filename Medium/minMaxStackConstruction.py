class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    def peek(self):
        # Time O(1) || Space O(1)
        if not self.stack:
            return None
        else:
            return self.stack[-1]

    def pop(self):
        # Time O(1) || Space O(1)
        if self.stack:
            self.minMaxStack.pop()
            return self.stack.pop()

        return None

    def push(self, number):
        # Time O(1) || Space O(1)
        currMinMax = {}
        if len(self.stack):
            prevMinMax = self.minMaxStack[-1]
            currMinMax["minVal"] = min(prevMinMax["minVal"], number)
            currMinMax["maxVal"] = max(prevMinMax["maxVal"], number)
        else:
            currMinMax = {"minVal": number, "maxVal": number}

        self.minMaxStack.append(currMinMax)
        self.stack.append(number)

    def getMin(self):
        # Time O(1) || Space O(1)
        return self.minMaxStack[-1]["minVal"]

    def getMax(self):
        # Time O(1) || Space O(1)
        return self.minMaxStack[-1]["maxVal"]
