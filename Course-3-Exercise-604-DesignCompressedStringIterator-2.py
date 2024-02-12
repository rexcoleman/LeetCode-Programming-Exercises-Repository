import itertools
from collections import deque


class StringIterator:

    def __init__(self, compressedString: str):
        self.s = compressedString
        self.s_parsed = deque()
        self.current_index = 0
        self.uncompressed_length = 0
        self.parse()

    def parse(self):
        cur = None
        for key, group in itertools.groupby(self.s, key=lambda x: x.isalpha()):
            if key:
                cur = ''.join(group)
            else:
                group_len = int(''.join(group))
                self.uncompressed_length += group_len
                self.s_parsed.append((cur, group_len))

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        cur_ch, cur_cnt = self.s_parsed[0]
        if cur_cnt > 0:
            self.s_parsed[0] = (cur_ch, cur_cnt - 1)
        if self.s_parsed[0][1] == 0:
            self.s_parsed.popleft()
        self.current_index += 1
        return cur_ch

    def hasNext(self) -> bool:
        return self.current_index < self.uncompressed_length



if __name__ == '__main__':

    commands = ["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
    values = [["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
    expected_output = [None, "L", "e", "e", "t", "C", "o", True, "d", True]

    string_iterator = StringIterator(values[0][0])
    output = [None,]
    for i in range(1, len(commands)):
        if commands[i] == "next":
            output.append(string_iterator.next())

        else:
            output.append(string_iterator.hasNext())

    print(f"\nTest Output: {output} \nExpected Output: {expected_output}")