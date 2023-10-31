from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if not head:
            return None

        left, right = head, head
        stop = False

        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers

            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next
        recurseAndReverse(right, m, n)
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
        return output
    while head:
        output.append(head.val)
        head = head.next

    return output



if __name__ == '__main__':
    # Inputs
    head_1 = [1, 2, 3, 4, 5]
    left_1 = 2
    right_1 = 4
    head_2 = [5]
    left_2 = 1
    right_2 = 1

    # Create linked lists
    ll_head_1 = listToLinkedList(head_1)
    ll_head_2 = listToLinkedList(head_2)

    # Print to test linked lists
    print(f"Print Test List 1: {linkedListToList(ll_head_1)}")
    print(f"Print Test List 2: {linkedListToList(ll_head_2)}")

    # Create solution objects for each test
    solution_1 = Solution()
    solution_2 = Solution()

    # Create Reversed Lists
    reversed_list_1 = solution_1.reverseBetween(ll_head_1, left_1, right_1)
    reversed_list_2 = solution_2.reverseBetween(ll_head_2, left_2, right_2)

    # Convert linked lists to arrays for output
    output_1 = linkedListToList(reversed_list_1)
    output_2 = linkedListToList(reversed_list_2)

    # Print test results
    print(f"Output 1: {output_1}: \nExpected Output 1: [1,4,3,2,5]")
    print(f"Output 2: {output_2}: \nExpected Output 2: [5]")