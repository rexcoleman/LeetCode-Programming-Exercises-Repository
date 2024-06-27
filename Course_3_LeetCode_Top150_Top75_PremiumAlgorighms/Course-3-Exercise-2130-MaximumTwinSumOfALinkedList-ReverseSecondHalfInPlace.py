import math
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
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_twin_sum = -math.inf
        slow, fast = head, head.next
        if not fast.next:
            return slow.val + fast.val
        while fast.next:
            slow = slow.next
            a = slow.val
            fast = fast.next.next
            b = fast.val
        prev, curr, new_end = slow, slow.next, slow.next
        c = prev.val
        d = curr.val
        prev.next = fast
        while curr:
            next_node = curr.next
            e = next_node.val if next_node else None
            curr.next = prev
            prev = curr
            f = prev.val
            curr = next_node
            g = curr.val if curr else None
        new_end.next = None
        slow = slow.next
        q = slow.val if slow else None
        temp = head
        r = temp.val
        while slow:
            max_twin_sum = max(max_twin_sum, temp.val + slow.val)
            temp = temp.next
            s = temp.val
            slow = slow.next
            t = slow.val if slow else None
        return max_twin_sum


if __name__ == '__main__':

    # Inputs and Expected Outputs
    head_1 = [5,4,2,1]
    expected_output_1 = 6
    head_2 = [4,2,2,3]
    expected_output_2 = 7
    head_3 = [1,100000]
    expected_output_3 = 100001
    head_4 = [47,22,81,46,94,95,90,22,55,91,6,83,49,65,10,32,41,26,83,99,14,85,42,99,89,69,30,92,32,74,9,81,5,9]
    expected_output_4 = 182

    # Construct Linked Lists
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()
    ll_1 = linked_list_1.listToLinkedList(head_1)
    ll_2 = linked_list_2.listToLinkedList(head_2)
    ll_3 = linked_list_3.listToLinkedList(head_3)
    ll_4 = linked_list_4.listToLinkedList(head_4)

    # Print to Test Linked Lists
    print(f"\nLinked List 1 Print Test: {linked_list_1.linkedListToList(ll_1)} \nExpected Output: {head_1}")
    print(f"\nLinked List 2 Print Test: {linked_list_2.linkedListToList(ll_2)} \nExpected Output: {head_2}")
    print(f"\nLinked List 3 Print Test: {linked_list_3.linkedListToList(ll_3)} \nExpected Output: {head_3}")
    print(f"\nLinked List 4 Print Test: {linked_list_4.linkedListToList(ll_4)} \nExpected Output: {head_4}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    solution_4 = Solution()
    test_1 = solution_1.pairSum(ll_1)
    test_2 = solution_2.pairSum(ll_2)
    test_3 = solution_3.pairSum(ll_3)
    test_4 = solution_4.pairSum(ll_4)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
    print(f"\nTest 4 Output: {test_4} \nExpected Output: {expected_output_4}")
