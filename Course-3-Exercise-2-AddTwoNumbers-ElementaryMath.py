from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, values):
        self.head = None
        if values:
            self.head = ListNode(values[0])
            current = self.head
            for val in values[1:]:
                current.next = ListNode(val)
                current = current.next

    def print_linked_list(self):
        output = []
        current = self.head
        while current:
            # print(current.val, end=" -> ")
            output.append(current.val)
            current = current.next
        # print("None")
        return output


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next

def list_to_linked_list(values):
    return LinkedList(values)


if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    l1 = list_to_linked_list([2, 4, 3])
    l2 = list_to_linked_list([5, 6, 4])
    print(f"List 1: {l1.print_linked_list()}")
    print(f"List 2: {l2.print_linked_list()}")
    result = solution.addTwoNumbers(l1.head, l2.head)
    result_linked_list = LinkedList([])
    result_linked_list.head = result
    print(f"Test 1: {result_linked_list.print_linked_list()}, Expected Result: [7, 0, 8]")


    # Test case 2
    l1 = list_to_linked_list([0])
    l2 = list_to_linked_list([0])
    print(f"List 1: {l1.print_linked_list()}")
    print(f"List 2: {l2.print_linked_list()}")
    result = solution.addTwoNumbers(l1.head, l2.head)
    result_linked_list = LinkedList([])
    result_linked_list.head = result
    print(f"Test 1: {result_linked_list.print_linked_list()}, Expected Result: [0]")


    # Test case 3
    l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_linked_list([9, 9, 9, 9])
    print(f"List 1: {l1.print_linked_list()}")
    print(f"List 2: {l2.print_linked_list()}")
    result = solution.addTwoNumbers(l1.head, l2.head)
    result_linked_list = LinkedList([])
    result_linked_list.head = result
    print(f"Test 1: {result_linked_list.print_linked_list()}, Expected Result: [8, 9, 9, 9, 0, 0, 0, 1]")
