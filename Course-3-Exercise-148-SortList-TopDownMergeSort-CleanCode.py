from typing import Optional


class ListNode:
    def __init__(self, val=0, left=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def listToLinkedList(self, values):
        if not values:
            return None
        self.head = ListNode(values[0])
        temp = self.head
        for i in range(1, len(values)):
            temp.next = ListNode(values[i])
            temp = temp.next
        return self.head


    def linkedListToList(self, head):
        output = []
        current = head
        while current:
            output.append(current.val)
            current = current.next
        return output

class Solution:

    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next
            # tnv = tail.next.val if tail.next.val is not None else None
            # tv = tail.val if tail.val is not None else None
            # h1 = None if h1 is None else h1.val
            # h2 = None if h2 is None else h2.val
        tail.next = h1 or h2
        return dummy.next


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        return self.merge(*map(self.sortList, (head, slow)))



if __name__ == '__main__':

    # Inputs and Expected Outputs:
    head_1 = [4, 2, 1, 3]
    expected_output_1 = [1, 2, 3, 4]
    head_2 = [-1, 5, 3, 4, 0]
    expected_output_2 = [-1, 0, 3, 4, 5]
    head_3 = []
    expected_output_3 = []

    # Construct Linked Lists
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    linked_list_3 = LinkedList()
    ll_1 = linked_list_1.listToLinkedList(head_1)
    ll_2 = linked_list_2.listToLinkedList(head_2)
    ll_3 = linked_list_3.listToLinkedList(head_3)

    # Print to Test Linked Lists
    print(f"\nLinked List 1 Print Test: {linked_list_1.linkedListToList(ll_1)}"
          f"\nExpected Result: {head_1}")
    print(f"\nLinked List 2 Print Test: {linked_list_2.linkedListToList(ll_2)}"
          f"\nExpected Result: {head_2}")
    print(f"\nLinked List 3 Print Test: {linked_list_3.linkedListToList(ll_3)}"
          f"\nExpected Result: {head_3}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.sortList(ll_1)
    test_2 = solution_2.sortList(ll_2)
    test_3 = solution_3.sortList(ll_3)

    # Print Results
    output_1 = linked_list_1.linkedListToList(test_1)
    output_2 = linked_list_2.linkedListToList(test_2)
    output_3 = linked_list_3.linkedListToList(test_3)

    print(f"\nTest 1 Result {output_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result {output_2} \nExpected Result: {expected_output_2}")
    print(f"\nTest 3 Result {output_3} \nExpected Result: {expected_output_3}")