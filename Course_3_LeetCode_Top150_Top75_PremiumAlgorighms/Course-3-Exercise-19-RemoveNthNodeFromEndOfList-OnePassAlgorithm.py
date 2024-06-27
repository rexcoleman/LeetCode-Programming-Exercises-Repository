from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head

        # This separates the two pointers by n (fast - slow == n)
        while n:
            fast = fast.next
            n -= 1

        # This is the case where we are removing the head (fast = length)
        if not fast:
            return head.next

        # This moves both pointers to the end of the list with fast - slow == n
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Change slow.next to remove Nth node from end
        slow.next = slow.next.next
        return head





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
    output = []
    if not head:
        return []

    while head:
        output.append(head.val)
        head = head.next

    return output


if __name__ == '__main__':

    # Inputs
    head_1 = [1, 2, 3, 4, 5]
    n_1 = 4
    head_2 = [1]
    n_2 = 1
    head_3 = [1, 2]
    n_3 = 1

    # Transform data from lists to linked lists
    ll_head_1 = listToLinkedList(head_1)
    ll_head_2 = listToLinkedList(head_2)
    ll_head_3 = listToLinkedList(head_3)

    # Print to test linked lists
    print(f"\nList 1: {linkedListToList(ll_head_1)} \nOriginal List: {head_1}")
    print(f"\nList 2: {linkedListToList(ll_head_2)} \nOriginal List: {head_2}")
    print(f"\nList 3: {linkedListToList(ll_head_3)} \nOriginal List: {head_3}")

    # Create solution objects for each test
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()

    # Remove Nth node from end
    test_1 = solution_1.removeNthFromEnd(ll_head_1, n_1)
    test_2 = solution_2.removeNthFromEnd(ll_head_2, n_2)
    test_3 = solution_3.removeNthFromEnd(ll_head_3, n_3)

    # Tranfrom data from linked lists to lists
    output_1 = linkedListToList(test_1)
    output_2 = linkedListToList(test_2)
    output_3 = linkedListToList(test_3)

    # Print results
    print(f"\nTest 1 Output: {output_1} \nExpected Output: [1,2,3,5]")
    print(f"\nTest 2 Output: {output_2} \nExpected Output: []")
    print(f"\nTest 3 Output: {output_3} \nExpected Output: [1]")