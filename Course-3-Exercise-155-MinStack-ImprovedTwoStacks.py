class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # We always put the number onto the main stack.
        self.stack.append(val)
        # If the min stack is empty, or this number is smaller than
        # the top of the min stack, put it on with a count of 1.

        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append([val, 1])
        # Else if this number is equal to what's currently at the top
        # of the min stack, then increment the count at the top by 1.
        elif val == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1

    def pop(self) -> None:
        # If the top of min stack is the same as the top of stack
        # then we need to decrement the count at the top by 1.
        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stack[-1][1] -= 1

        # If the count at the top of min stack is now 0, then remove
        # that value as we're done with it.
        if self.min_stack[-1][0] == 0:
            self.min_stack.pop()

        # And like before, pop the top of the main stack.
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]



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
