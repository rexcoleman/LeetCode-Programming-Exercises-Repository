from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def listToLinkedList(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        temp = head
        for i in range(1,len(values)):
            temp.next = ListNode(values[i])
            temp = temp.next
        return head

    def linkedListToList(self, head):
        output = []
        if not head:
            return output
        temp = head
        while temp:
            output.append(temp.val)
            temp = temp.next
        return output

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: return None if there is only one node.
        if head.next == None:
            return None
        count = 0
        p1 = p2 = head

        # First pass, count the number of nodes in the linked list using 'p1'.
        while p1:
            count += 1
            p1 = p1.next

        # Get the index of the node to be deleted.
        middle_index = count // 2

        # Second pass, let 'p2' move toward the predecessor of the middle node.
        for _ in range(middle_index - 1):
            p2 = p2.next

        # Delete the middle node and return 'head'.
        p2.next = p2.next.next
        return head


if __name__ == '__main__':

    # Inputs and Expected Outputs
    head_1 = [1, 3, 4, 7, 1, 2, 6]
    expected_output_1 = [1, 3, 4, 1, 2, 6]
    head_2 = [1, 2, 3, 4]
    expected_output_2 = [1, 2, 4]
    head_3 = [2, 1]
    expected_output_3 = [2]

    # Construct LinkedLists
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    linked_list_3 = LinkedList()
    ll_1 = linked_list_1.listToLinkedList(head_1)
    ll_2 = linked_list_2.listToLinkedList(head_2)
    ll_3 = linked_list_3.listToLinkedList(head_3)

    # Print to Test LinkLists
    print(f"\nLinked List 1 Print Test: {linked_list_1.linkedListToList(ll_1)} \nExpected Output: {head_1}")
    print(f"\nLinked List 2 Print Test: {linked_list_2.linkedListToList(ll_2)} \nExpected Output: {head_2}")
    print(f"\nLinked List 3 Print Test: {linked_list_3.linkedListToList(ll_3)} \nExpected Output: {head_3}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.deleteMiddle(ll_1)
    test_2 = solution_2.deleteMiddle(ll_2)
    test_3 = solution_3.deleteMiddle(ll_3)

    # Print Results
    output_1 = linked_list_1.linkedListToList(test_1)
    output_2 = linked_list_2.linkedListToList(test_2)
    output_3 = linked_list_3.linkedListToList(test_3)
    print(f"\nTest 1 Output: {output_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {output_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {output_3} \nExpected Output: {expected_output_3}")