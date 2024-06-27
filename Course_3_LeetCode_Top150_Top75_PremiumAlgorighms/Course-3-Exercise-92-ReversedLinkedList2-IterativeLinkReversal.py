from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
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
    if not head:
        return None
    output = []
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
    print(f"List 1: {linkedListToList(ll_head_1)}")
    print(f"List 2: {linkedListToList(ll_head_2)}")

    # Create solution objects for each test
    solution_1 = Solution()
    solution_2 = Solution()

    # Reverse linked lists
    reversed_list_1 = solution_1.reverseBetween(ll_head_1, left_1, right_1)
    reversed_list_2 = solution_2.reverseBetween(ll_head_2, left_2, right_2)

    # Convert linked lists to output lists
    output_1 = linkedListToList(reversed_list_1)
    output_2 = linkedListToList(reversed_list_2)

    # Print results
    print(f"Output 1: {output_1}: \nExpected Output 1: [1,4,3,2,5]")
    print(f"Output 2: {output_2}: \nExpected Output 2: [5]")