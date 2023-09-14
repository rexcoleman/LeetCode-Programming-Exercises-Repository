# FIFO: first item we insert will be the first item we take out
class Queue:

    def __init__(self):
        # use one stack for the operations
        self.stack = []

    # adding an item to the queue is O(1) operation
    def enqueue(self, data):
        self.stack.append(data)

    # NOTE: we use two stacks again but instead of explicitly defining the second stack we
    # use the call-stack of program (stack memory or execution stack)
    def dequeue(self):

        # base case for the recursive method calls the first item
        # is what we are after (this is what we need for queue's dequeue operation)
        if len(self.stack) == 1:
            return self.stack.pop()

        # we keep popping the items until we find the last one
        item = self.stack.pop()

        # we call the method recursively until we find the first item we have inserted
        dequeued_item = self.dequeue()

        # after we find the item we have to insert the items one by one
        self.stack.append(item)

        # this is the item we are looking for (this is what has been popped off in the
        # stack.size() == 1 operation
        return dequeued_item

if __name__ == '__main__':

    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(5)
    queue.enqueue(20)
    print(queue.dequeue())
    queue.enqueue(100)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

