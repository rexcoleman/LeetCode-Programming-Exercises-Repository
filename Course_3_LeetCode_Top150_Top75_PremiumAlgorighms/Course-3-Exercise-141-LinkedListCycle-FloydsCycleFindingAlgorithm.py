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

    def append(self, x):
        new_node = ListNode(x)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print_list(self, head):
        temp = self.head
        for i in range(len(head) + 1):
            if temp is None:
                return
            print(temp.val)
            temp = temp.next

    def pos(self, pos):
        if pos < 0 or pos >= self.length:
            return
        temp = self.head
        for i in range(pos):
            temp = temp.next
        self.tail.next = temp

    def construct_ll(self, head, pos):
        if len(head) < 1:
            return
        for i in range(1, len(head)):
            self.append(head[i])
            if i == len(head) - 1:
                self.pos(pos)

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

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

    linked_list2 = LinkedList(head2[0])
    linked_list2.construct_ll(head2, pos2)
    linked_list2.print_list(head2)
    outcome2 = solution.hasCycle(linked_list2.head)
    print(f"Outcome2: {outcome2}")

    linked_list3 = LinkedList(head3[0])
    linked_list3.construct_ll(head3, pos3)
    linked_list3.print_list(head3)
    outcome3 = solution.hasCycle(linked_list3.head)
    print(f"Outcome3: {outcome3}")



