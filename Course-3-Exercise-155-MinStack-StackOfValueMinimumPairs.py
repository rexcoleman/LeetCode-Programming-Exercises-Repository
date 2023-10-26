class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # If the stack is empty, then the min value
        # must just be the first value we add
        if not self.stack:
            self.stack.append((val, val))
            return
        current_min = self.stack[-1][1]
        self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]



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
