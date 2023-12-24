from collections import deque


class RecentCounter:

    def __init__(self):
        self.counter = deque()
    def ping(self, t: int) -> int:
        self.counter.append(t)
        low_range = t - 3000
        while self.counter[0] < low_range:
            self.counter.popleft()
        return len(self.counter)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


if __name__ == '__main__':

    # Inputs and Expected Outputs
    commands = ["RecentCounter", "ping", "ping", "ping", "ping", "ping"]
    values = [[],[642],[1849],[4921],[5936],[5957]]
    expected_output = [None, 1, 2, 1, 2, 3]

    recent_counter = RecentCounter()
    len_commands = len(commands)
    output = [None,]

    for i in range(1, len_commands):
        output.append(recent_counter.ping(values[i][0]))

    print(f"\nOutput: {output} \nExpected Output: {expected_output}")
