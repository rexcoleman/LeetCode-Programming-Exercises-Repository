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
        self.head = ListNode(values[0])
        temp = self.head
        for i in range(1, len(values)):
            temp.next = ListNode(values[i])
            temp = temp.next
        return self.head

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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = dummy2.next
        return dummy1.next


if __name__ == '__main__':

    # Inputs and Expected Outputs
    head_1 = [1, 2, 3, 4, 5]
    expected_output_1 = [1, 3, 5, 2, 4]
    head_2 = [2, 1, 3, 5, 6, 4, 7]
    expected_output_2 = [2, 3, 6, 7, 1, 5, 4]
    head_3 = [1, 2, 3, 4, 5, 6, 7, 8]
    expected_output_3 = [1, 3, 5, 7, 2, 4, 6, 8]

    # Construct Linked Lists
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    linked_list_3 = LinkedList()
    ll_1 = linked_list_1.listToLinkedList(head_1)
    ll_2 = linked_list_2.listToLinkedList(head_2)
    ll_3 = linked_list_3.listToLinkedList(head_3)

    # Print to Test Linked Lists
    print(f"\nLinked List 1 Print Test: {linked_list_1.linkedListToList(ll_1)} \nExpected Output: {head_1}")
    print(f"\nLinked List 2 Print Test: {linked_list_2.linkedListToList(ll_2)} \nExpected Output: {head_2}")
    print(f"\nLinked List 3 Print Test: {linked_list_3.linkedListToList(ll_3)} \nExpected Output: {head_3}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.oddEvenList(ll_1)
    test_2 = solution_2.oddEvenList(ll_2)
    test_3 = solution_3.oddEvenList(ll_3)

    output_1 = linked_list_1.linkedListToList(test_1)
    output_2 = linked_list_2.linkedListToList(test_2)
    output_3 = linked_list_3.linkedListToList(test_3)

    # Print Results
    print(f"\nTest 1 Output: {output_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {output_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {output_3} \nExpected Output: {expected_output_3}")
