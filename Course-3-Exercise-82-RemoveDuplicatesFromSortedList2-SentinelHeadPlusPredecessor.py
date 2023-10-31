from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Sentinal node
        sentinel = ListNode(0, head)

        # predecessor = the last node
        # before the sublist of duplicates
        predecessor = sentinel

        while head:
            # if it's a beginning of duplicates sublist
            # skip all duplicates
            if head.next and head.val == head.next.val:
                # move till the end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next
                # skip all duplicates
                predecessor.next = head.next
            # otherwise, move predecessor
            else:
                predecessor = predecessor.next

            # move forward
            head = head.next

        return sentinel.next




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
    head_1 = [1, 2, 3, 3, 4, 4, 5]
    head_2 = [1, 1, 1, 2, 3]

    # Transform lists to linked lists
    ll_head_1 = listToLinkedList(head_1)
    ll_head_2 = listToLinkedList(head_2 )

    # Print to test linked lists
    print(f"\nList 1: {linkedListToList(ll_head_1)} \nOriginal List: {head_1}")
    print(f"\nList 2: {linkedListToList(ll_head_2)} \nOriginal List: {head_2}")

    # Create solution objects for each test
    solution_1 = Solution()
    solution_2 = Solution()

    # Remove duplicates
    test_1 = solution_1.deleteDuplicates(ll_head_1)
    test_2 = solution_2.deleteDuplicates(ll_head_2)

    # Transfrom linked lists to lists for output
    output_1 = linkedListToList(test_1)
    output_2 = linkedListToList(test_2)

    # Print test results
    print(f"\nTest 1 Output: {output_1} \nExpected Output: [1,2,5]")
    print(f"\nTest 2 Output: {output_2} \nExpected Output: [2,3]")
