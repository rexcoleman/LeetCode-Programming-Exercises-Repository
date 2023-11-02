from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Before and after are the two pointers used to create two linked lists
        # Before_head and after_head are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        # Last node of "after" list would also be ending node of the reformed list
        after.next = None
        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = after_head.next

        return before_head.next



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
    head_1 = [1,4,3,2,5,2]
    x_1 = 3
    head_2 = [2,1]
    x_2 = 2

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
    test_1 = solution_1.partition(ll_head_1, x_1)
    test_2 = solution_2.partition(ll_head_2, x_2)

    # Transform linked lists into output lists
    output_1 = linkedListToList(test_1)
    output_2 = linkedListToList(test_2)

    # Print test results
    print(f"\nTest 1: {output_1} \nExpected Output: [1,2,2,4,3,5]")
    print(f"\nTest 2: {output_2} \nExpected Output: [1,2]")

