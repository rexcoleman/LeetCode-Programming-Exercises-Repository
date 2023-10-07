class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Maintain an unchanging reference to the node ahead
        # of the return node
        prehead = ListNode(-1)
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point
        # Connect the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2
        return prehead.next


def list_to_linkedlist(list):
    dummy = ListNode(0)
    current = dummy
    for val in list:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == '__main__':
    solution = Solution()

    list1_1 = [1, 2, 4]
    list1_2 = [1, 3, 4]
    list2_1 = []
    list2_2 = []
    list3_1 = []
    list3_2 = [0]

    linked_list1_1 = list_to_linkedlist(list1_1)
    linked_list1_2 = list_to_linkedlist(list1_2)
    linked_list2_1 = list_to_linkedlist(list2_1)
    linked_list2_2 = list_to_linkedlist(list2_2)
    linked_list3_1 = list_to_linkedlist(list3_1)
    linked_list3_2 = list_to_linkedlist(list3_2)

    outcome_linkedlist_1 = solution.mergeTwoLists(linked_list1_1, linked_list1_2)
    outcome_linkedlist_2 = solution.mergeTwoLists(linked_list2_1, linked_list2_2)
    outcome_linkedlist_3 = solution.mergeTwoLists(linked_list3_1, linked_list3_2)

    outcome_list_1 = linkedlist_to_list(outcome_linkedlist_1)
    outcome_list_2 = linkedlist_to_list(outcome_linkedlist_2)
    outcome_list_3 = linkedlist_to_list(outcome_linkedlist_3)

    print(f"Outcome1: {outcome_list_1}")
    print(f"Outcome2: {outcome_list_2}")
    print(f"Outcome3: {outcome_list_3}")