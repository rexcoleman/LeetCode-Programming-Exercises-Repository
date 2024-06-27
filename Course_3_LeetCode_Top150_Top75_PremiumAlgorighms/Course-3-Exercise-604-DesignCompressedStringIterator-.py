from collections import deque


class StringIterator:

    def __init__(self, compressedString: str):
        self.compString = compressedString
        self.char_queue = deque()
        self.curr_char = ''
        self.curr_count = 0
        for i in range(len(compressedString)):
            self.char_queue.append(compressedString[i])

    def next(self) -> str:
        if self.char_queue or self.curr_count > 0:
            if self.curr_count == 0:
                self.curr_char = self.char_queue.popleft()
                while self.char_queue and self.char_queue[0].isdigit():
                    self.curr_count *= 10
                    self.curr_count += int(self.char_queue.popleft())
            self.curr_count -= 1
            return self.curr_char
        else:
            return " "

    def hasNext(self) -> bool:
        if self.curr_count > 0 or self.char_queue and self.char_queue[0]:
            return True
        else:
            return False



if __name__ == '__main__':

    commands = ["StringIterator","next","next","next","hasNext","next","next","next","next","next","next","next","hasNext","next","next","next","next","next","hasNext","next","next","next","next","next","hasNext","next","next","next","next","hasNext","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","hasNext","next","hasNext","next","next","next","next","next","next","hasNext","next","next","next","next","next","next","next","next","next","next","next","next","next","next","hasNext","next","next","next","hasNext","next","next","hasNext","next","next","next","next","next"]
    values = [["x6"],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    expected_output = [None,"x","x","x",True,"x","x","x"," "," "," "," ",False," "," "," "," "," ",False," "," "," "," "," ",False," "," "," "," ",False," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",False," ",False," "," "," "," "," "," ",False," "," "," "," "," "," "," "," "," "," "," "," "," "," ",False," "," "," ",False," "," ",False," "," "," "," "," "]

    string_iterator = StringIterator(values[0][0])
    output = [None,]
    for i in range(1, len(commands)):
        if commands[i] == "next":
            output.append(string_iterator.next())

        else:
            output.append(string_iterator.hasNext())

    print(f"\nTest Output: {output} \nExpected Output: {expected_output}")