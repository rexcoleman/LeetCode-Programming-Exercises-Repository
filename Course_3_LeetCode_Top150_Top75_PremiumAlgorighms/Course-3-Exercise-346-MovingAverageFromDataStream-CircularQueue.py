from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        queue = self.queue
        hed = self.head
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        window_sum = self.window_sum

        return self.window_sum / min(self.size, self.count)


if __name__ == '__main__':

    commands = ["MovingAverage", "next", "next", "next", "next"]
    inputs = [[3], [1], [10], [3], [5]]
    expected_output = [None, 1.0, 5.5, 4.66667, 6.0]

    moving_average = MovingAverage(inputs[0][0])
    output = [None,]

    for _ in range(1, len(commands)):
        if commands[_] == 'next':
            result = moving_average.next(inputs[_][0])
            formatted_result = float("{:.5f}".format(result))
            output.append(formatted_result)

    print(f"\nTest Output: {output} \nExpected Output: {expected_output}")