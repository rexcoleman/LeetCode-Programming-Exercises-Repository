class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:

    def __init__(self, x):
        new_node = ListNode(x)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self, head):
        temp = self.head
        for i in range(len(head)+1):
            if temp is None:
                return
            print(temp.val)
            temp = temp.next

    def append(self, x):
        new_node = ListNode(x)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def pos(self, pos):
        if pos < 0 or pos >= self.length:
            return
        temp = self.head
        for _ in range(pos):
            temp = temp.next
        self.tail.next = temp

    def construct_ll(self, head, pos):
        if len(head) < 1:
            return
        for i in range(1, len(head)):
            self.append(head[i])
            if i == len(head) - 1:
                self.pos(pos)

    def clear_ll(self):
        while self.length > 0:
            self.pop_first()



class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False


if __name__ == '__main__':
    solution = Solution()
    head1 = [3, 2, 0, -4]
    pos1 = 1
    head2 = [1, 2]
    pos2 = 0
    head3 = [1]
    pos3 = -1


    linked_list1 = LinkedList(head1[0])
    linked_list1.construct_ll(head1, pos1)
    linked_list1.print_list(head1)
    outcome1 = solution.hasCycle(linked_list1.head)
    print(f"Outcome1: {outcome1}")
    # linked_list1.clear_ll()

    linked_list2 = LinkedList(head2[0])
    linked_list2.construct_ll(head2, pos2)
    linked_list2.print_list(head2)
    outcome2 = solution.hasCycle(linked_list2.head)
    print(f"Outcome2: {outcome2}")
    # linked_list2.clear_ll()

    linked_list3 = LinkedList(head3[0])
    linked_list3.construct_ll(head3, pos3)
    linked_list3.print_list(head3)
    outcome3 = solution.hasCycle(linked_list3.head)
    print(f"Outcome3: {outcome3}")
    # linked_list3.clear_ll()
