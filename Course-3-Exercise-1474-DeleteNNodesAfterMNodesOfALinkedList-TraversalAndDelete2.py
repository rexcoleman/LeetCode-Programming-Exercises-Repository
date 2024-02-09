class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def listToLinkedList(self, values):
        if not values:
            return
        self.head = ListNode(values[0])
        temp = self.head
        for i in range(1, len(values)):
            temp.next = ListNode(values[i])
            temp = temp.next
        return self.head


    def linkedLIstToList(self, head):
        output = []
        if not head:
            return output
        while head:
            output.append(head.val)
            head = head.next
        return output

class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        i = 0
        while head:
            if i < m-1:
                i += 1
            else:
                j = 0
                while j < n and head.next:
                    head.next = head.next.next
                    j += 1
                i = 0
            head = head.next
        return dummy.next


if __name__ == '__main__':

    # Inputs and Expected Outputs
    head_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    m_1 = 2
    n_1 = 3
    expected_output_1 = [1, 2, 6, 7, 11, 12]
    head_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    m_2 = 1
    n_2 = 3
    expected_output_2 = [1, 5, 9]

    # Construct LinkedLists
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    ll_1 = linked_list_1.listToLinkedList(head_1)
    ll_2 = linked_list_2.listToLinkedList(head_2)

    # Print to Test Linked Lists
    print(f"/nLinked List 1 Print Test: {linked_list_1.linkedLIstToList(ll_1)} \nExpected Output: {head_1}")
    print(f"/nLinked List 2 Print Test: {linked_list_2.linkedLIstToList(ll_2)} \nExpected Output: {head_2}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()

    # Print Results