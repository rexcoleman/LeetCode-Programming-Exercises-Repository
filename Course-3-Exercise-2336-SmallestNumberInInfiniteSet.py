import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.is_present = set()
        self.added_integers: [int] = []
        self.current_integer = 1

    def popSmallest(self) -> int:
        # If there are numbers in the min-heap,
        # top element is lowest among all the available numbers.
        if len(self.added_integers):
            answer = heapq.heappop(self.added_integers)
            self.is_present.remove(answer)
        # Otherwise, the smallest number of large positive set
        # denoted by 'current_integer' is the answer.
        else:
            answer = self.current_integer
            self.current_integer += 1
        return answer

    def addBack(self, num: int) -> None:
        if self.current_integer <= num or num in self.is_present:
            return
        # We push 'num' in the min-heap if it isn't already present.
        heapq.heappush(self.added_integers, num)
        self.is_present.add(num)


if __name__ == '__main__':

    commands = ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest",
     "popSmallest", "popSmallest"]
    values = [[], [2], [], [], [], [1], [], [], []]
    expected_results = [[],[],[1],[2],[3],[],[1],[4],[5]]

    sis = SmallestInfiniteSet()
    for i in range(1, len(commands)):
        if commands[i] == "popSmallest":
            command = sis.popSmallest()
            print(f"\nInteger Popped: {command} \nExpected Result: {expected_results[i][0]}")
        else:
            sis.addBack(values[i][0])

