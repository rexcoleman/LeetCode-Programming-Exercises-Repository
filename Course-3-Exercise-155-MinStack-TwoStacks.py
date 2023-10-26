class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]



if __name__ == '__main__':

    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    test_1 = minStack.getMin()
    print(f"Test 1: {test_1}, Expected Result: -3")
    minStack.pop()
    test_2 = minStack.top()
    print(f"Test 2: {test_2}, Expected Result: 0")
    test_3 = minStack.getMin()
    print(f"Test 3: {test_3}, Expected Result: -2")
