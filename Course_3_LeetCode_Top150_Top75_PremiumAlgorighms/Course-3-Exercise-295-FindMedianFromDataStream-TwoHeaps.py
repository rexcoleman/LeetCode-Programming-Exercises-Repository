from heapq import heappush, heappushpop


class MedianFinder:

    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap


    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            # Move the largest element from the max heap (small) to the min heap (large)
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            # Move the smallest element from the min heap (large) to the max heap (small)
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


if __name__ == '__main__':

    # Inputs and Expected Outputs
    commands = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    values = [[], [1], [2], [], [3], []]
    expected_output = [None, None, None, 1.5, None, 2.0]

    median_finder = MedianFinder()
    output = [None]

    for i in range(1, len(commands)):
        if commands[i] == "addNum":
            median_finder.addNum(values[i][0])
            output.append(None)
            # print(median_finder.small + median_finder.large)
        else:
            output.append(median_finder.findMedian())
    print(f"\nTest Output: {output} \nExpected Output: {expected_output}")

