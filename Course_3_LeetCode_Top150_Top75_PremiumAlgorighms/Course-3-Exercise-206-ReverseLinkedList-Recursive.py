from typing import Optional

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

    def lindedListToList(self, node):
        output = []
        if not node:
            return output
        temp = node
        while temp:
            output.append(temp.val)
            temp = temp.next
        return output


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head


if __name__ == '__main__':

    # Inputs and Expected Outputs
    head_1 = [1, 2, 3, 4, 5]
    expected_output_1 = [5, 4, 3, 2, 1]
    head_2 = [1, 2]
    expected_output_2 = [2, 1]
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
    print(f"\nLinked List 1 Print Test: {linked_list_1.lindedListToList(ll_1)} \nExpected Result: {head_1}")
    print(f"\nLinked List 2 Print Test: {linked_list_2.lindedListToList(ll_2)} \nExpected Result: {head_2}")
    print(f"\nLinked List 3 Print Test: {linked_list_3.lindedListToList(ll_3)} \nExpected Result: {head_3}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.reverseList(ll_1)
    test_2 = solution_2.reverseList(ll_2)
    test_3 = solution_3.reverseList(ll_3)

    # Translate to Output Lists
    output_1 = linked_list_1.lindedListToList(test_1)
    output_2 = linked_list_2.lindedListToList(test_2)
    output_3 = linked_list_3.lindedListToList(test_3)

    # Print Results
    print(f"\nTest 1 Output: {output_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {output_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {output_3} \nExpected Output: {expected_output_3}")
