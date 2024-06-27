from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def listToLinkedList(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        temp = head
        for i in range(1, len(values)):
            temp.next = ListNode(values[i])
            temp = temp.next
        return head

    def linkedListToList(self, head):
        output = []
        if not head:
            return output
        while head:
            output.append(head.val)
            head = head.next
        return output


class Solution:
    def reverseLinkedList(self, head, k):
        # Reverse k nodes of the given linked list.
        # This function assumes that the list contains at least k nodes.
        new_head, pointer = None, head
        while k:
            # Keep track of the next node to process in the original list
            next_node = pointer.next

            # Insert the node pointed to by "ptr" at the beginning of the reversed list
            pointer.next = new_head
            new_head = pointer

            # Move on to the next node
            pointer = next_node

            # Decrement the count of nodes to be reversed by 1
            k -= 1

        # Return the head of the reversed list
        return new_head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pointer = head
        ktail = None

        # Head of the final, moified linked list
        new_head = None
        # Keep going until there are nodes in the list
        while pointer:
            count = 0

            # Start counting nodes from the head
            pointer = head

            # Find the head of the next k nodes
            while count < k and pointer:
                pointer = pointer.next
                count += 1

            # If we counted k nodes, reverse them
            if count == k:

                # Reverse k nodes and get the new head
                revHead = self.reverseLinkedList(head, k)

                # new_head is the head of the final linked list
                if not new_head:
                    new_head = revHead

                # ktail is the tail of the previous block of
                # reversed k nodes
                if ktail:
                    ktail.next = revHead

                ktail = head
                head = pointer

        # attach the final, possibly un-reversed portion
        if ktail:
            ktail.next = head

        return new_head if new_head else head



if __name__ == '__main__':

    # Inputs and Expected Outputs
    head_1 = [1, 2, 3, 4, 5]
    k_1 = 2
    expected_output_1 = [2, 1, 4, 3, 5]
    head_2 = [1, 2, 3, 4, 5]
    k_2 = 3
    expected_output_2 = [3, 2, 1, 4, 5]

    # Construct Linked Lists
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    ll_1 = linked_list_1.listToLinkedList(head_1)
    ll_2 = linked_list_2.listToLinkedList(head_2)

    # Print to Test Linked Lists
    print(f"\nList 1 Print Test: {linked_list_1.linkedListToList(ll_1)}")
    print(f"\nList 2 Print Test: {linked_list_2.linkedListToList(ll_2)}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.reverseKGroup(ll_1, k_1)
    test_2 = solution_2.reverseKGroup(ll_2, k_2)

    # Print Results
    output_1 = linked_list_1.linkedListToList(test_1)
    output_2 = linked_list_2.linkedListToList(test_2)

    print(f"\nTest 1 Output: {output_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {output_2} \nExpected Output: {expected_output_2}")