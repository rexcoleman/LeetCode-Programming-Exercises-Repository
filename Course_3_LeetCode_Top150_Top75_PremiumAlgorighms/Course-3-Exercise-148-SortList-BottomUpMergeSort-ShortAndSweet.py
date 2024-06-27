from typing import Optional


class ListNode:
    def __init__(self, val=0, left=None):
        self.val = val
        self.next = None

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
        current = head
        while current:
            output.append(current.val)
            current = current.next
        return output

class Solution:

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        # Grab sublists of size 1, then 2, then 4, etc, until fully merged
        steps = 1
        while True:
            # Record the progress of the current pass into a single semi sorted list by updating
            # the next of the previous node (or the dummy on the first loop)
            prev = dummy

            # Keep track of how much is left to process on this pass of the list
            remaining = prev.next

            # While the current pass though the list has not been completed
            num_loops = 0
            while remaining:
                num_loops += 1

                # Split 2 sublists of steps length from the front
                sublists = [None, None]
                sublists_tail = [None, None]
                for i in range(2):
                    sublists[i] = remaining
                    substeps = steps
                    while substeps and remaining:
                        substeps -= 1
                        sublists_tail[i] = remaining
                        remaining = remaining.next
                    # Ensure the subslist (if one was made) is terminated
                    if sublists_tail[i]:
                        sublists_tail[i].next = None

                # We have two sublists of (upto) length step that are sorted, merge them onto
                # the end into a single list of (upto) step * 2
                while sublists[0] and sublists[1]:
                    if sublists[0].val <= sublists[1].val:
                        prev.next = sublists[0]
                        sublists[0] = sublists[0].next
                    else:
                        prev.next = sublists[1]
                        sublists[1] = sublists[1].next
                    prev = prev.next

                # One list has been finished, attach what ever is left of the other to the end
                if sublists[0]:
                    prev.next = sublists[0]
                    prev = sublists_tail[0]
                else:
                    prev.next = sublists[1]
                    prev = sublists_tail[1]

            # Double the steps each go around
            steps *= 2

            # If the entire list was fully processed in a single loop, it means we've completely sorted the list and are done
            if 1 >= num_loops:
                return dummy.next



if __name__ == '__main__':

    # Inputs and Expected Outputs:
    head_1 = [4, 2, 1, 3]
    expected_output_1 = [1, 2, 3, 4]
    head_2 = [-1, 5, 3, 4, 0]
    expected_output_2 = [-1, 0, 3, 4, 5]
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
    print(f"\nLinked List 1 Print Test: {linked_list_1.linkedListToList(ll_1)}"
          f"\nExpected Result: {head_1}")
    print(f"\nLinked List 2 Print Test: {linked_list_2.linkedListToList(ll_2)}"
          f"\nExpected Result: {head_2}")
    print(f"\nLinked List 3 Print Test: {linked_list_3.linkedListToList(ll_3)}"
          f"\nExpected Result: {head_3}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.sortList(ll_1)
    test_2 = solution_2.sortList(ll_2)
    test_3 = solution_3.sortList(ll_3)

    # Print Results
    output_1 = linked_list_1.linkedListToList(test_1)
    output_2 = linked_list_2.linkedListToList(test_2)
    output_3 = linked_list_3.linkedListToList(test_3)

    print(f"\nTest 1 Result {output_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result {output_2} \nExpected Result: {expected_output_2}")
    print(f"\nTest 3 Result {output_3} \nExpected Result: {expected_output_3}")