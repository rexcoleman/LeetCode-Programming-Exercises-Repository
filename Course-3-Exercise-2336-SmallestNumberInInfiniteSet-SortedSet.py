import heapq
from sortedcontainers import SortedSet


class SmallestInfiniteSet:

    def __init__(self):
        self.added_integers = SortedSet()
        self.current_integer = 1

    def popSmallest(self) -> int:
        # If there are numbers in the sorted-set,
        # top element is lowest among all the available numbers.
        if len(self.added_integers):
            answer = self.added_integers[0]
            self.added_integers.discard(answer)
        # Otherwise, the smallest number of large positive set
        # denoted by 'current_integer' is the answer.
        else:
            answer = self.current_integer
            self.current_integer += 1
        return answer

    def addBack(self, num: int) -> None:
        if self.current_integer <= num or num in self.added_integers:
            return
        # We push 'num' in the sorted-set if it isn't already present.
        self.added_integers.add(num)


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

