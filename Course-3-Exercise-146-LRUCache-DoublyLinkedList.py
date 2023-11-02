class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)
        node = ListNode(key, value)
        self.dic[key] = node
        self.add(node)

        if len(self.dic) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]


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
    # LRUCache.put(1, 1)



    # Expected Output
    # [null, null, null, 1, null, -1, null, -1, 3, 4]