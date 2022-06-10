class MinStack:
    minVal = 0
    
    def __init__(self):
        ''' 
        Create two stacks... one for regular and one for the minimum value 
        '''
        self.stack = []
        self.minStack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # If minStack is non-empty, take the minimum of input value and the top of the minStak
        if self.minStack:
            val = min(val, self.minStack[-1])
        
        self.minStack.append(val)

       
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    
    def top(self) -> int:
        return self.stack.pop()

    def getMin(self) -> int:
        return self.minStack.pop()
    
