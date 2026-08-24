class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minValue = None

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        if (self.minValue is None) or (value <= self.minValue):
            self.minStack.append(value)
            self.minValue = value


    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] == self.getMin():
            self.minStack.pop()
            if not self.minStack:
                self.minValue = None
            else:
                self.minValue = self.minStack[-1]
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()