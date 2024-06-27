from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        window_sum = sum(queue[-size:])

        return window_sum / min(len(queue), size)


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