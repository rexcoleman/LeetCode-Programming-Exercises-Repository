import collections

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        self.dic.move_to_end(key)
        return self.dic[key]


    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)
        self.dic[key] = value
        if len(self.dic) > self.capacity:
            self.dic.popitem(False)



    def add(self, node):
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



if __name__ == '__main__':

    commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    values = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    expected_output = [None, None, None, 1, None, -1, None, -1, 3, 4]

    lru_cache = LRUCache(int(values[0][0]))
    for i in range(1, len(commands)):
        e_output = expected_output[i] if not None else "None"
        if commands[i] == "put":
            output = lru_cache.put(int(values[i][0]), int(values[i][1]))
            print(f"\nOutput: {output} \nExpected Output: {e_output}")
        else:
            lru_cache.get(int(values[i][0]))
            output = lru_cache.get(values[i][0])
            print(f"\nOutput: {output} \nExpected Output: {e_output}")
