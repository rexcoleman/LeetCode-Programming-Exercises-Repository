from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Base case
        if not head:
            return None
        # close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        # find new tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        new_tail = head
        for i in range(n - (k % n) - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # Break the ring
        new_tail.next = None

        return new_head




def listToLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    temp = head
    for i in range(1, len(values)):
        temp.next = ListNode(values[i])
        temp = temp.next

    return head

def linkedListToList(head):
    if not head:
        return []
    output = []
    while head:
        output.append(head.val)
        head = head.next

    return output



if __name__ == '__main__':

    # Inputs
    head_1 = [1, 2, 3, 4, 5]
    k_1 = 2
    head_2 = [0, 1, 2]
    k_2 = 4

    # Transform inputs into linked lists
    ll_head_1 = listToLinkedList(head_1)
    ll_head_2 = listToLinkedList(head_2)

    # Print to test linked lists
    print(f"\nList 1: {linkedListToList(ll_head_1)} \nOriginal list: {head_1}")
    print(f"\nList 2: {linkedListToList(ll_head_2)} \nOriginal list: {head_2}")

    # Create solution objects for each test
    solution_1 = Solution()
    solution_2 = Solution()

    # Rotate linked lists
    test_1 = solution_1.rotateRight(ll_head_1, k_1)
    test_2 = solution_2.rotateRight(ll_head_2, k_2)

    # Transform linked lists into output lists
    output_1 = linkedListToList(test_1)
    output_2 = linkedListToList(test_2)

    # Print test results
    print(f"\nTest 1: {output_1} \nExpected Output: [4,5,1,2,3]")
    print(f"\nTest 2: {output_2} \nExpected Output: [2,0,1]")

