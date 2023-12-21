# Definition for singly-linked list.
from typing import List, Optional
from queue import PriorityQueue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def listToLinkedList(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        temp = head
        for i in range(1, len(values)):
            temp.next = ListNode(values[i])
            temp = temp.next
        return head

    def linkedListToList(self, head):
        output = []
        if not head:
            return output
        while head:
            output.append(head.val)
            head = head.next
        return output


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = point = ListNode(0)
        q = PriorityQueue()
        index = 0  # Tiebreaker
        for l in lists:
            if l:
                a = l.val
                q.put((l.val, index, l))
                index += 1
        while not q.empty():
            val, _, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                b = node.val
                q.put((node.val, index, node))
                index += 1
        return head.next


if __name__ == '__main__':

    # Inputs and Expected Outputs
    lists_1 = [[1, 4, 5], [1, 3, 4], [2, 6]]
    expected_output_1 = [1, 1, 2, 3, 4, 4, 5, 6]
    lists_2 = []
    expected_output_2 = []
    lists_3 = [[]]
    expected_output_3 = []

    # Transform Nested Lists to Linked Lists
    linked_lists_1 = LinkedList()
    linked_lists_2 = LinkedList()
    linked_lists_3 = LinkedList()
    ll_1 = [linked_lists_1.listToLinkedList(list) for list in lists_1]
    ll_2 = [linked_lists_2.listToLinkedList(list) for list in lists_2]
    ll_3 = [linked_lists_3.listToLinkedList(list) for list in lists_3]

    # Print to Test Link List Construction
    print_ll_1 = [linked_lists_1.linkedListToList(list) for list in ll_1]
    print_ll_2 = [linked_lists_2.linkedListToList(list) for list in ll_2]
    print_ll_3 = [linked_lists_3.linkedListToList(list) for list in ll_3]
    print(f"\nList 1 Original List: {print_ll_1} \nLinkedList Print Test: {print_ll_1}")
    print(f"\nList 2 Original List: {print_ll_2} \nLinkedList Print Test: {print_ll_2}")
    print(f"\nList 3 Original List: {print_ll_3} \nLinkedList Print Test: {print_ll_3}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.mergeKLists(ll_1)
    test_2 = solution_2.mergeKLists(ll_2)
    test_3 = solution_3.mergeKLists(ll_3)
    output_1 = linked_lists_1.linkedListToList(test_1)
    output_2 = linked_lists_2.linkedListToList(test_2)
    output_3 = linked_lists_3.linkedListToList(test_3)
    print(f"\nTest 1 Output: {output_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {output_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {output_3} \nExpected Output: {expected_output_3}")


